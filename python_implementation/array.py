# 배열(Array)

#####################################################################
# 배열은 같은 종류의 데이터를 순차적으로 저장하는 자료구조이다. 
# python에서는 list로 구현이 되어있다. 배열은 index를 통한 직접 접근이 가능하다.
# 장점: 빠른 접근이 가능하다.
# 단점: 데이터 추가와 삭제에 비용이 많이 든다. 데이터 추가 시, 공간이 많이 필요하며 삭제 시 빈 공간이 생겨 이를 관리해주어야 한다. 더불어 길이 조절이 어렵다.
#####################################################################

# 1차원 배열 = 리스트
data = [1,2,3,4,5]
string1 = 'Hello World'
print(data[3]) # 4
print(string1[3]) # l

# 2차원 배열
data2 = [[1,2,3],[4,5,6],[7,8,9]]
print(data[1][0]) # 4

# 예제
# 특정 alpabet의 빈도 수 측정 함수
def find_alphabet(dataset, alphabet):
    count = 0
    for data in dataset:
        for i in range(len(data)):
            if data[i] == alphabet:
                count += 1
    return count