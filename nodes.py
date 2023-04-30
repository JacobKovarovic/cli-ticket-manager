class TreeNode():
    def __init__(self, data, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getHeight(self):
        return self._getHeight(self)
    
    def _getHeight(self, currNode):
        if currNode == None or (currNode.leftChild == None and currNode.rightChild == None):
            return 0
        leftHeight = self._getHeight(currNode.leftChild)
        rightHeight = self._getHeight(currNode.rightChild)
        if leftHeight > rightHeight:
            return 1 + leftHeight
        return 1 + rightHeight

    def clone(self):
        return TreeNode(self.data, self.leftChild, self.rightChild)
    
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