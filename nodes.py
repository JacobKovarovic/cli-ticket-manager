class TreeNode():
    def __init__(self, data, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getHeight(self):
        if self.leftChild == None and self.rightChild == None:
            return 0
        if self.leftChild == None:
            return 1 + self.rightChild.getHeight()
        if self.rightChild == None:
            return 1 + self.leftChild.getHeight()
        if self.leftChild.getHeight() > self.rightChild.getHeight():
            return 1 + self.leftChild.getHeight()
        return 1 + self.rightChild.getHeight()

    def clone(self):
        return TreeNode(self.data)
    
    def __str__(self):
        return str(self.data) + "(" + str(self.leftChild) + ", " + str(self.rightChild) + ")"
    
    def isComplete(self):
        if self.getHeight() == 0:
            return True
        if self.leftChild == None:
            return False
        if self.rightChild == None:
            return False
        if self.leftChild.getHeight() == self.rightChild.getHeight():
            return True and self.leftChild.isComplete() and self.rightChild.isComplete()
        return False