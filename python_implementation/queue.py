# 큐(Queue)

#####################################################################
# 큐는 먼저 넣은 데이터를 가장 먼저 꺼내는 데이터 구조이다.
# First-In, First-Out(FIFO) / Last-In, Last-Out(LILO)

# 기능
# Enqueue: 큐에 데이터를 넣는 기능. python list의 append()와 유사.
# Dequeue: 큐에서 데이터를 꺼내는 기능. python list의 pop(0)와 유사.
#####################################################################

# 종류
# python에서는 queue 라이브러리를 제공한다. 하지만 대부분의 큐와 관련된 자료구조는 list를 통해 구현이 가능하다.
import queue

# Queue(): 일반적인 큐 자료구조
data_queue = queue.Queue()
data_queue.put(1) # 1
data_queue.put(2) # 1-2
data_queue.put(3) # 1-2-3
data_queue.get() # 1
data_queue.get() # 2

# LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조(stack과 동일)
data_queue = queue.LifoQueue()
data_queue.put(1) # 1
data_queue.put(2) # 2-1
data_queue.put(3) # 3-2-1
data_queue.get() # 3
data_queue.get() # 2

# PriorityQueue(): 데이터마다 우선순위를 지정하여 정렬된 큐로, 우선순위가 높은 순으로 출력하는 자료 구조
data_queue = queue.PriorityQueue()
data_queue.put((10,1)) # (10,1) 첫번째 원소가 우선순위를 의미.
data_queue.put((5,2)) # (5,2)-(10,1)
data_queue.put((15,3)) # (5,2)-(10,1)-(15,3)
data_queue.get() # (5,2)
data_queue.get() # (10,1)

# 리스트로 Queue 구현
class ListQueue:
    def __init__(self):
        self.my_list = list()
    def put(self, element): # Enqueue 기능
        self.my_list.append(element)
    def get(self): #Dequeue 기능
        return self.my_list.pop(0)
    def qsize(self): # queue의 길이 반환
        return len(self.my_list)

# 리스트로 PriorityQueue 구현
class ListPriorityQueue:
    def __init__(self):
        self.my_list = list()
    def put(self, element):
        self.my_list.append(element)
        self.my_list.sort(key = lambda x: x[0]) # element의 첫 번째 원소가 작은 순서로 우선순위 정렬 예시
    def get(self):
        return self.my_list.pop(0)
    def qsize(self):
        return len(self.my_list)