# 힙(heap)

#####################################################################
# 최대값 및 최소값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한 자료구조
# 힙에는 다음과 같이 2가지 종류가 존재
# 최대 힙: 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰 힙
# 최소 힙: 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작은 힙
# 원소 값의 대소관계는 오로지 부모 노드와 자식 노드 간에만 성립하며, 특히 형제 사이에는 대소관계가 정해지지 않는다.
# 힙에서는 가장 높은(혹은 가장 낮은) 우선순위를 가지는 노드가 항상 root 노드에 오게 되는 특징이 있으며, 이를 응용하면 우선순위 큐와 같은 추상적인 자료형 구현 가능.
# 힙이 시간 복잡도는 삽입, 삭제 모두 O(logn). 
###################################################################

# MaxHeap
# 힙은 리스트로 구현함.
# i번째 노드의 왼쪽 자식노드의 위치는 (2i+1)이 되며 오른쪽 자식노드의 위치는 (2i+2)가 되고 부모 노드의 위치는 (i-1/2)가 된다.
class MaxHeap(object):

    def __init__(self):
        self.queue = []
    
    def parent(self, index):
        return (index-1) // 2

    def leftchild(self, index):
        return 2*index + 1
    
    def rightchild(self, index):
        return 2*index + 2

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def insert(self, n):
        # 맨 마지막에 삽입할 원소를 임시로 추가한다.
        self.queue.append(n)
        last_index = len(self.queue) - 1
        # 부모를 타고 올라가면서 크기를 비교해준다.
        while last_index >= 0:
            parent_index = self.parent(last_index)
            if parent_index >= 0 and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break
    
    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return -1
        self.swap(0, last_index)
        maxv = self.queue.pop()
        self.maxHeapify(0) # root에서부터 재정렬
        print(maxv)
        return maxv

    # 임시 root 값부터 자식들과 값을 비교해나가며 재정렬하는 함수
    def maxHeapify(self, i):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)
        max_index = i # 더 큰 값의 index를 넣어준다.

        if left_index <= len(self.queue)-1 and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= len(self.queue)-1 and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index
        #만약 자신이 가장 큰 것이 아니라면 heapify
        if max_index != i:
            self.swap(i, max_index)
            self.maxHeapify(max_index)

    def printHeap(self):
        print(self.queue)

if __name__ == "__main__":
    mh = MaxHeap()
    mh.insert(1)
    mh.insert(3)
    mh.insert(11)
    mh.insert(6)
    mh.insert(5)
    mh.insert(2)
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
