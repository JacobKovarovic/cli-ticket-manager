class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class TreeNode(Node):
    def __init__(self, data, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild