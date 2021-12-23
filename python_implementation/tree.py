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

# Binary Search Table(BST)
