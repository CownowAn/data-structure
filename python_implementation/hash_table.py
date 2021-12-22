# 해쉬 테이블(Hash Table)

#####################################################################
# 해쉬 구조란, key와 value 쌍으로 이루어진 자료구조이다. key를 이용하여 데이터를 찾으음으로써 속도를 빠르게 만드는 구조이다.
# python는 dictionary 타입이 해쉬 테이블과 같은 구조이다.
# 기본적으로는 배열로 미리 Hash Table 크기만큼 생성해서 사용한다. 이렇게 하면 공간은 많이 사용하나 시간이 빠르다는 장점이 있다.
# 검색이 많이 필요한 경우, 저장/삭제/읽기가 많은 경우, 캐쉬를 구현할 때 주로 사용된다.

# 장단점
# 장점: 데이터 저장/검색 속도가 빠르다. 또한 해쉬는 key에 대한 데이터가 있는지 (중복)확인이 쉽다.
# 단점: 일반적으로 저장 공간이 더 많이 필요하다. 여러 key에 해당하는 주소가 동일할 경우, 출돌을 해결하기 위한 별도의 자료구조가 필요하다. (충돌 해결 알고리즘)

# 시간복잡도
# 일반적인 경우(충돌이 없는 경우): O(1)
# 최악의 경우(모든 경우에서 충돌이 발생하는 경우): O(N)

# 용어
# 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것.
# 해쉬 함수(Hash Function): 특정 연산을 이용하여 key값을 받아서 value를 가진 공간의 주소로 바꾸어주는 함수.
# 해쉬 테이블(Hash Table): 해쉬 구조를 사용하는 자료구조.
# 해쉬 값(해쉬 주소, Hash Value or Address): key값을 해쉬 함수에 넣어서 얻은 주소값. 이 값을 통해 슬롯을 찾아간다.
# 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
#####################################################################

### 본 예제에서는 키 생성 함수를 python 기본 라이브러리인 hash() 함수를 사용할 것이다.
# 해당 함수는 실행마다 값이 달라질 수 있다. 사실 Hash Function은 보안 분야에서 많이 사용된다.
# 예를 들어 SHA(Secure Hash Algorithm은 어떤 데이터도 고정된 크기의 유일한 값으로 리턴해주기 때문에 많이 사용된다. ###

# SHA-1: Hash Value의 크기를 160으로 고정한는 알고리즘.
import hashlib # hashlib는 SHA 함수들을 가지고 있는 라이브러리

data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

data2 = 'hello world'.encode()
hash_object2 = hashlib.sha1()
hash_object2.update(data2)
hex_dig2 = hash_object2.hexdigest()
print(hex_dig2)
# SHA-1 대신 SHA-256을 사용하면 Hash value의 크기가 256이기 때문에 더 안전하다. 위 코드에서 sha1() 대신 sha256()을 사용하면 된다.

# python의 dictionary
# key, value 구조의 데이터를 가지는 형태로 구성.
dic = {'name':'Kang', 'phone':'01012345678','birth':'000101'}

# dictionary 생성
a = {1:'a'}

# key(2), value(b) 쌍 추가
a[2] = 'b'
print(a) # {1:'a',2:'b'}

# key(3), value([1,2,3]) 추가
a[3] = [1,2,3]
print(a) # {1:'a',2:'b',3:[1,2,3]}

# key 2인 요소 삭제
del a[2]
print(a) # {1:'a',3:[1,2,3]}

# key 1인 요소 접근
a[1] # 'a'

# key list 만들기
a.keys() # dict_keys([1,3])

# key:value 쌍 얻기
a.items() # dict_items([(1,'a'),(3,[1,2,3])])

# key로 value 얻기
a.get(1) # 'a'

# key:value 쌍 모두 지우기
a.clear()
print(a) # {}

# 중복 주의. dictionary의 key 값이 중복되면, 가장 뒤쪽이 key:value 쌍만을 가지고 기존의 쌍은 무시.
# key 값으로 list는 불가능. key 값으로 쓸 수 있는 것은 변하지 않는 값에 해당.
a = {1:'a',1:'b'}
print(a) # {1:'b'}

# List로 Hash Table 만들기
class HashTable:
    # 해당 해쉬테이블의 공간은 8자리이다.
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])
    
    # 해당 테이블의 해쉬 함수는 간단하게 key % 8로 설정.
    def hash_function(self, key):
        return key % 8
    
    # 해쉬 키를 생성하는 것은 python 기본 라이브러리의 hash 함수 사용. hash 함수는 랜덤 연산작용으로 실행시킬때마다 값이 달라질 수 있음.
    # insert 함수를 통해 key, value 쌍을 넣을 수 있음.
    def insert(self, key, value):
        hash_value = self.hash_function(hash(key))
        self.hash_table[hash_value] = value

    # read 함수를 통해 key 값을 이용하여 vlaue 값을 얻을 수 있음.
    def read(self, key):
        hash_value = self.hash_function(hash(key))
        return self.hash_table[hash_value]

    def print(self):
        print(self.hash_table)

# List로 만든 개선된 Hash Table(충돌 해결 알고리즘)
# 충돌을 해결하기 위한 방법으로는 크게 3가지가 존재.
# 1) Chaining 기법
# Open Hashing 기법 중 하나: Hash Table 저장 공간 외에 공간을 더 추가해서 사용하는 방법.
# 충돌 발생 시, Linked List로 데이터를 추가로 뒤에 연결시키는 방법.
# 이 방식은 끝 없이 key, value 쌍들을 넣을 수 있으나 공간 효율성이 떨어진다는 단점이 있다.
# 하나의 hash value index에만 들어간다면 불균형한 구조가 될 가능성이 있다.
class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])
    def hash_function(self, key):
        #Custom Hash Function
        return key % 8
    def insert(self, key, value):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            # 해당 hash value index를 이미 사용하고 있는 경우(충돌 시)
            for i in range(len(self.hash_table[hash_value])):
                # 이미 같은 key 값이 존재하는 경우 -> value 교체
                # 이 때 0은 key, 1은 value 값이 존재하는 index
                if self.hash_table[hash_value][i][0] == gen_key:
                    self.hash_table[hash_value][i][1] = value
                    return
                # 값은 key 값이 존재하지 않는 경우에는 [key, value]를 해당 index에 삽입
                self.hash_table[hash_value].append([gen_key, value])
        else:
            # 해당 hash_value를 사용하고 있지 않은 경우
            self.hash_table[hash_value] = [[gen_key, value]]
    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            # 해당 hash value index에 데이터가 존재할 때,
            for i in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][i][0] == gen_key:
                    # key와 동일한 경우 -> 해당 value return
                    return self.hash_table[hash_value][i][1]
                # 동일한 key가 존재하지 않으면 None return
                return None
        else:
            # 해당 hash value index에 데이터가 없을 때, None return
            return None
    def print(self):
        print(self.hash_table)

# 2) Linear Probing 기법
# Close Hashing 기법 중 하나: Hash Table 저장 공간 안에서 충돌 문제를 해결하는 방법.
# 충돌이 일어나면, 해당 hash value(hash address)의 다음 index부터 맨 처음 나오는 빈 공간에 저장하는 기법.(저장 공간 활용도의 증가)
# 이 알고리즘은 미리 지정한 hash table의 자리 수를 넘어감녀 충돌이 일어나게 된다는 단점이 있다.
class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])
    def hash_function(self, key):
        #Custom Hash Function
        return key % 8
    def insert(self, key, value):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            # 해당 hash value index를 이미 사용하고 있는 경우(충돌 시)
            for i in range(hash_value, len(self.hash_table)):
                # 해당 hash value index부터 마지막 index까지 돌면서 비어있거나 key가 같은 값을 찾는다.
                if self.hash_table[i] == 0:
                    # 해당 index가 비어 있을 때,
                    self.hash_table[i] = [[gen_key, value]]
                    return
                elif self.hash_table[i][0] == gen_key:
                    # 이미 같은 key 값이 존재하는 경우 덮어쓰기
                    self.hash_table[i][1] = value
                    return
                else:
                    # 해당 hash value를 사용하고 있지 않은 경우
                    self.hash_table[hash_value] = [[gen_key, value]]
    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            # 해당 hash value index에 데이터가 존재할 때,
            for i in range(hash_value, len(self.hash_table)):
                if self.hash_table[i] == 0:
                # 비어 있는 경우
                    return None
                elif self.hash_table[i][0] == gen_key:
                    # key와 동일할 경우 -> 해당 value return
                    return self.hash_table[i][1]
        else:
            # 해당 hash value index에 데이터가 없을 때,
            return None
    def print(self):
        print(self.hash_table)

# 3) 공간을 확장하는 방법
# 2번에서 사용한 Linear Probing 방식에서 공간을 늘린다면 1번에 비해 균형적인 구조로 사용이 가능하다.
# n을 생성자의 매개변수로 사용해서 받고, 해당 n을 큰 수로 늘린다면 많은 공간을 사용할 수 있다.
class HashTable:
    def __init__(self, n):
        self.n = n
        self.hash_table = list([0 for i in range(n)])
    def hash_function(self, key):
        # Custom Hash Function
        return key % self.n