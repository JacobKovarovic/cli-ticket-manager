from nodes import TreeNode

class AbstractHeap():
    def __init__(self, sourceCollection = None):
        self.size = 0
        self.head = None
        if sourceCollection != None:
            if not iter(sourceCollection):
                raise TypeError("Source collection must be iterable")
            for item in sourceCollection:
                self.push(item)

    def __str__(self):
        return str(map(str, self))

class MinHeap(AbstractHeap):
    def __init__(self, sourceCollection = None):
        super(sourceCollection)

    def push(self, item):
        if self.head == None:
            self.head = TreeNode(item)
            return
        _pushNode(self.head, TreeNode(item))

    def _pushNode(self, currNode, newNode):
        if type(newNode) != type(TreeNode()):
            raise TypeError("Cannot push non-TreeNode object")
        if currNode.leftChild == None:
            currNode.leftChild = newNode
            return
        if currNode.rightChild == None:
            currNode.rightChild = newNode
            return
        leftHeight = currNode.leftChild.getHeight()
        rightHeight = currNode.rightChild.getHeight()
        if leftHeight == rightHeight:
            self._pushNode(currNode.leftChild, newNode)
        if leftHeight > rightHeight:
            self._pushNode(currNode.rightChild, newNode)