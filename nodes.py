class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class TreeNode(Node):
    def __init__(self, data, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getHeight(self):
        if self.leftChild = None and self.rightChild = None:
            return 0
        if self.leftChild.getHeight() > self.rightChild.getHeight()
            return 1 + self.leftChild.getHeight()
        return 1 + self.rightChild.getHeight()