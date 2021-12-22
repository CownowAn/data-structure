# 연결 리스트(Linked List)

#####################################################################
# 연결 리스트는 배열과 달리 연결되지 않고, 떨어진 곳에 존재하는 데이터를 경로로 지정하여 관리하는 데이터 구조이다.
# python에서는 list 자료구조가 linked list 기능을 모두 지원한다.

# 기능
# Node: 데이터 저장 단위로, 데이터 값+포인터로 구성.
# Pointer: 각 노드 안에서 다음이나 이전 Node의 주소를 가지는 값.

# 장단점
# 장점: 미리 데이터 공간을 할당할 필요가 없다.
# 단점: 연결을 위한 별도 데이터 공간이 필요하므로 공간적 효율이 낮다. 또한 데이터를 찾는데 있어 접근성이 좋지 않으므로 속도가 느리다.
# 중간 데이터 삭제 시, 앞 뒤 Node를 모두 고려하여 재구성하는 코드를 작성해야 한다.
#####################################################################

# python으로 Node 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# python으로 Linked List 구현 (간단한 코드만을 구현. 중간 데이터 삽입 코드 X)
class LinkedList:
    def __init__(self):
        self.head = None
    
    # data를 받아서 Node를 만들어 연결 리스트에 추가시켜주는 add 함수
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
    
    # Node의 data값을 통해 연결 리스트에서 제거하는 delete 함수
    def delete(self, data):
        node = self.head
        if node.data == data:
            self.head = node.next
            del node
        else:
            while node.next:
                next_node = node.next
                if next_node.data == data:
                    node.next = next_node.next
                    del next_node
                else:
                    node = node.next
    
    # data값으로 Node를 찾아주는 find 함수
    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
    
    # 현재 연결 리스트 내 모든 Node의 data값을 출력하는 print 함수
    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

# 사용 예시
ll = LinkedList() # 연결 리스트 ll 선언
ll.add(1) # data가 1인 Node1 추가
ll.add(2) # data가 2인 Node2 추가
ll.add(3) # data가 3인 Node3 추가
ll.print() # 1 2 3

ll.delete(2) # data가 2인 Node2 삭제
ll.print() # 1 3

ll.delete(1) # data가 1인 Node1 삭제
ll.print() # 3

ll.delete(3) # data가 3인 Node3 삭제
ll.print() # None

# Doubly Linked List
# 이중 연결 리스트라고도 하는 Doubly Linked List는 양방향의 Node 주소 값을 모두 가지고 있어서 양방향으로 탐색이 가능하다는 장점을 가진 Linked List이다.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # 기존의 Linked List의 Node에서 prev라는 이전의 Node를 가리키는 변수를 추가하면 된다.

# Linked List class와 비교하여, 초기화 함수에 tail 변수가 추가된 점과 add 시, tail 변수를 고려해준다는 점이 다르다. 나머지는 동일하다.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node.prev = node
            node.next = new_node
            self.tail = new_node
