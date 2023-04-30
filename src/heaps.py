from src.nodes import TreeNode

class _AbstractHeap():
    def __init__(self, sourceCollection = None):
        self.size = 0
        self.head = None
        if sourceCollection != None:
            print("Adding source collection!")
            for item in sourceCollection:
                self.push(item)

    def __str__(self):
        if self.isEmpty():
            raise KeyError("Heap is empty")
        return self._toStringPreorder(self.head)
    
    def __iter__(self):
        if self.head == None:
            raise KeyError("Heap is empty")
        def preorder(currNode):
            data = [currNode.data]
            if currNode.leftChild != None:
                data += preorder(currNode.leftChild)
            if currNode.rightChild != None:
                data += preorder(currNode.rightChild)
            return data
        return iter(preorder(self.head))

    def _toStringPreorder(self, currNode):
        if currNode == None:
            return ""
        if currNode.leftChild == None and currNode.rightChild == None:
            return str(currNode.data)
        return str(currNode.data) + "(" + self._toStringPreorder(currNode.leftChild) + ", " + self._toStringPreorder(currNode.rightChild) + ")"
        
    def printLikeTree(self):
        self.head.printLikeTree()

    def isEmpty(self):
        return self.head == None
    
    def clear(self):
        while not self.isEmpty():
            self.pop()

    def getDeepestParent(self):
        if self.isEmpty():
            raise KeyError("Heap is empty")
        if self.head.getHeight() == 1:
            return self.head
        return self._getDeepestParent(self.head)
    
    def _getDeepestParent(self, currNode):
        if currNode.leftChild == None and currNode.rightChild == None:
            return None
        if currNode.rightChild == None:
            return currNode
        if currNode.isComplete():
            getRightmost = lambda node: node if node.rightChild.rightChild == None else getRightmost(node.rightChild)
            deepestParent = getRightmost(currNode)
            return deepestParent
        deepestParent = self._getDeepestParent(currNode.rightChild)
        if deepestParent == None:
            deepestParent = self._getDeepestParent(currNode.leftChild)
        return deepestParent

    def _removeDeepest(self):
        if self.getDeepestParent().rightChild == None:
            self.getDeepestParent().leftChild = None
            return
        self.getDeepestParent().rightChild = None

    def getDeepestNode(self):
        deepestParent = self.getDeepestParent()
        if deepestParent.rightChild == None:
            return deepestParent.leftChild
        return deepestParent.rightChild

class MinHeap(_AbstractHeap):
    def __init__(self, sourceCollection = None):
        super().__init__(sourceCollection)

    def clone(self):
        print("Cloning!")
        print([item for item in self])
        return MinHeap([item for item in self])

    def push(self, item):
        self.size += 1
        if self.isEmpty():
            self.head = TreeNode(item)
            return
        self._push(self.head, TreeNode(item))

    def _push(self, currNode, newNode):
        if newNode.data < currNode.data:
            tempData = currNode.data
            currNode.data = newNode.data
            self._push(self.head, TreeNode(tempData))
            return
        if currNode.leftChild == None:
            currNode.leftChild = newNode
            return
        if currNode.rightChild == None:
            currNode.rightChild = newNode
            return
        if currNode.isComplete():
            self._push(currNode.leftChild, newNode)
            return
        if currNode.leftChild.isComplete():
            self._push(currNode.rightChild, newNode)
            return
        self._push(currNode.leftChild, newNode)

    def pop(self):
        if self.isEmpty():
            return KeyError("Heap is empty")
        returnItem = self.head.data
        if self.head.getHeight() == 0:
            self.head = None
            return returnItem
        deepestNode = self.getDeepestNode()
        self.head.data = deepestNode.data
        self._removeDeepest()
        self._reheapify(self.head)
        self.size -= 1
        return returnItem

    def _reheapify(self, currNode):
        if currNode.leftChild == None and currNode.rightChild == None:
            return
        if currNode.rightChild == None:
            if currNode.leftChild.data < currNode.data:
                temp = currNode.data
                currNode.data = currNode.leftChild.data
                currNode.leftChild.data = temp
            return
        if currNode.leftChild.data < currNode.rightChild.data:
            if currNode.leftChild.data < currNode.data:
                temp = currNode.data
                currNode.data = currNode.leftChild.data
                currNode.leftChild.data = temp
                return self._reheapify(currNode.leftChild)
            return
        if currNode.rightChild.data < currNode.data:
            temp = currNode.data
            currNode.data = currNode.rightChild.data
            currNode.rightChild.data = temp
            return self._reheapify(currNode.rightChild)
        return

    def peek(self):
        return self.head.data