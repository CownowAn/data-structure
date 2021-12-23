# 트리(Tree)

#####################################################################
# 비선형 자료구조에 대항하며 데이터의 표현에 포커스가 맞추어져 있다.
# 트리의 가장 윗 부분에 있는 노드를 root 노드라고 하며 edge로 연결된 하위 노드를 자식(child) 노드라고 부른다.
# 자식 노드를 기준으로 보면 edge로 연결된 상위 노드를 부모(parent)노드라고 부른다.
# 자식 노드를 가지고 있지 않는 노드는 단말(leaf)노드라고 부른다.

# 이진 트리(Binary Tree)
# 이진트리란, 하나의 노드에 2개의 서브 노드가 있는 트리를 의미한다.
# 포화이진트리: 모든 level과 칸이 노드로 가득 차 있는 이진트리
# 완전이진트리: 모든 칸이 노드로 가득 차 있지는 않지만 위에서 아래로, 왼쪽에서 오른쪽 순서대로 노드가 들어가있는 이진트리

# 트리에서 원하는 값을 찾기 위해서는 노드와 노드를 이동하며 트리를 순회해야하는데,
# 트리의 순회에는 전위, 중위, 후위 세 가지 방법이 있다. 기준은 root 노드를 언제 방문하는지이다.
#####################################################################

# Binary Tree
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
    
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0
        return leftDepth+1 if leftDepth>rightDepth else rightDepth+1

    # 중위순회
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal
    
    # 전위순회
    def preorder(self):
        travesre = []
        travesre.append(self.data)
        if self.left:
            travesre += self.left.preorder()
        if self.right:
            travesre += self.right.preorder()
        return travesre

    # 후위순회
    def postorder(self):
        traverse = []
        if self.left:
            traverse += self.left.postorder()
        if self.right:
            traverse += self.right.postorder()
        traverse.append(self.data)
        return traverse

class BinaryTree:
    def __init__(self, r):
        self.root = r
    
    def size(self):
        if self.roof:
            return self.root.size()
        else:
            return 0
    
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
    
    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []
    
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

# 이진탐색트리(Binary Search Table(BST))
# 이진탐색트리는 모든 노드 n에 대해서 '모든 왼쪽 자식들 <= n <= 모든 오른쪽 자식들'속성이 참인 것을 말한다.
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key<self.key:
            if self.left: self.left.insert(key, data)
            else: self.left = Node(key, data)
        elif key>self.key:
            if self.right: self.right.insert(key, data)
            else: self.right = Node(key, data)
        else:
            raise KeyError("Key %d is already exist!" % key)

    def lookup(self, key, parent=None):
        if key<self.key:
            if self.left: return self.left.lookup(key, self)
            else: return None, None
        elif key>self.key:
            if self.right: return self.right.lookup(key, self)
            else: return None, None
        else:
            return self, parent

    def countChildren(self):
        count = 0
        if self.left: count += 1
        if self.right: count+= 1
        return count

class BinSearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root: return self.root.insert(key, data)
        else: self.root = Node(key, data)

    def lookup(self, key):
        if self.root: return self.root.lookup(key)
        else: return None, None
    
    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # [Case 1]: The simplest case of no children
            if nChildren == 0:
                # 만약 parent가 있으면 
                # node가 왼쪽 자식인지 오른쪽 자신인지 판단하여 parent.left or parent.right를 None으로 하여
                # Leaf Node였던 자식을 트리에서 끊어내어 없앤다.
                if parent:
                    if parent.left == node: parent.left = None
                    else: parent.right = None
                # 만약 parent가 없으면 (node는 root인 경우) self.root를 None으로 하여 빈트리로 만든다.
                else:
                    self.root = None
            # [Case 2]: When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽 자식인지 오른쪽 자식인지 판단하여 그 자식을 어떤 변수가 가리키도록 한다.
                # 만약 parent가 있으면 node가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node의 자리에 넣는다.
                if parent:
                    if node.left: # node의 자식이 왼쪽에 위치하는 경우
                        if parent.left == node: parent.left = node.left
                        else: parent.right = node.left
                    else: # node의 자식이 오른쪽에 위치하는 경우
                        if parent.left == node: parent.left = node.right
                        else: parent.right = node.right
                # 만약 parent가 없으면 (node는 root인 경우) self.root에 위에서 가리킨 자식을 대신 넣는다.
                else:
                    if node.left: self.root = node.left
                    else: self.root = node.right
            # [Case 3]: When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent가 node를 가리키도록 하고 successor는 node의 오른쪽 자식 서브트리의 root node를 가리키도록 한다.
                # successor로부터 왼쪽 자식의 링크를 반복하여 따라감으로써 순환문이 종료할 때 successor는 node의 오른쪽 자식 서브트리의 최소값을,
                # 그리고 parent는 그 node의 부모 node를 가리키도록 찾아낸다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node에 방금 찾은 successor의 key와 data를 대입한다.
                node.key = successor.key
                node.data = successor.data
                # 이제 successor가 parent의 왼쪽 자식인지 오른쪽 자식인지 파악하여
                # 그에 따라 parent.left 또는 parent.right를 successor가 가지고 있던(없을 수도 있지만) 자식을 가리키도록 한다.
                if parent.left == successor:
                    if successor.left: parent.left = successor.left
                    elif successor.right: parent.left = successor.right
                    else: parent.left = None
                else:
                    if successor.left: parent.right = successor.left
                    elif successor.right: parent.right = successor.right
                    else: parent.right = None
            return True
        else:
            return False
            
                



