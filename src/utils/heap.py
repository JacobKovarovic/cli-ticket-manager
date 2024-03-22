from .node import TreeNode

class _AbstractHeap():
    """
    Abstract heap class.
    Uses binary tree implementation.
    Contains methods for finding the deepest node in the heap (for deletion),
    and stores the pointer to the top of the heap and heap size
    """

    def __init__(self, sourceCollection = None):
        """
        Heap constructor.
        Create heapified representation of source collection 
        iterable or empty heap.
        """
        self.size = 0
        self.root = None
        if sourceCollection != None:
            print("Adding source collection!")
            for item in sourceCollection:
                self.push(item)

    def __str__(self):
        """
        Precondition: Heap is not empty
        Return: String representation of heap in preorder
        """
        if self.isEmpty():
            raise KeyError("Heap is empty")
        return self._toStringPreorder(self.root)
    
    def __iter__(self):
        """
        Precondition: Heap is not empty
        Return: Iterable list of heap items
        """
        if self.root == None:
            raise KeyError("Heap is empty")
        def preorder(currNode):
            data = [currNode.data]
            if currNode.leftChild != None:
                data += preorder(currNode.leftChild)
            if currNode.rightChild != None:
                data += preorder(currNode.rightChild)
            return data
        return iter(preorder(self.root))

    def _toStringPreorder(self, currNode):
        """
        Return: A string representation of heap in preorder form.
        """
        if currNode == None:
            return ""
        if currNode.leftChild == None and currNode.rightChild == None:
            return str(currNode.data)
        return str(currNode.data) + "(" + self._toStringPreorder(currNode.leftChild) + ", " + self._toStringPreorder(currNode.rightChild) + ")"
        
    def printLikeTree(self):
        """
        Return: String representation of minheap that visually resembles a tree
        Calls the printLikeTree() TreeNode function on root
        """
        self.root.printLikeTree()

    def isEmpty(self):
        """
        Return: True if minheap is empty, false otherwise.
        """
        return self.root == None
    
    def clear(self):
        """
        Postcondition: Heap is made empty.
        """
        while not self.isEmpty():
            self.pop()

    def getDeepestParent(self):
        """
        Precondition: Heap is not empty
        Return: Parent of deepest node in heap.
        This is necessary for removing the deepest node, as setting the deepest node to None
        rather than its parent's child value to None will result in a copy of the child node being created and
        set to None rather than the node in the heap.
        """
        if self.isEmpty():
            raise KeyError("Heap is empty")
        if self.root.getHeight() == 1:
            return self.root
        return self._getDeepestParent(self.root)
    
    def _getDeepestParent(self, currNode):
        """
        Helper function for self.getDeepestParent()
        Precondition: Heap height > 1
        """
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
        """
        Private function for deleting deepest node.
        Precondition: Heap height is greater than 0
        Postcondition: Deepest node is removed from heap
        / parent of deepest node's child value is set to None
        for that node
        """
        if self.getDeepestParent().rightChild == None:
            self.getDeepestParent().leftChild = None
            return
        self.getDeepestParent().rightChild = None

    def getDeepestNode(self):
        """
        Return the deepest node in the tree.
        Precondition: Heap height > 0
        """
        deepestParent = self.getDeepestParent()
        if deepestParent.rightChild == None:
            return deepestParent.leftChild
        return deepestParent.rightChild

class MinHeap(_AbstractHeap):
    """
    MinHeap extends _AbstractHeap.
    For each node in the minheap, the value of its children must both be less than it or None
    The root of the minheap is always the smallest value in the minheap.
    """
    def __init__(self, sourceCollection = None):
        """
        Create a minheap.
        Pass the sourcecollection to parent constructor.
        """
        super().__init__(sourceCollection)

    def clone(self):
        """
        Return: Copy of minheap
        """
        print("Cloning!")
        print([item for item in self])
        return MinHeap([item for item in self])

    def push(self, item):
        self.size += 1
        if self.isEmpty():
            self.root = TreeNode(item)
            return
        self._push(self.root, TreeNode(item))

    def _push(self, currNode, newNode):
        """
        Helper function for self.push()
        Precondition: Heap is not empty
        Postcondition: New node is placed at valid position in heap
        """
        if newNode.data < currNode.data:
            tempData = currNode.data
            currNode.data = newNode.data
            self._push(self.root, TreeNode(tempData))
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
        """
        Precondition: Heap is not empty
        Postcondition: Min element is removed, new min element is placed at root
        """
        if self.isEmpty():
            return KeyError("Heap is empty")
        returnItem = self.root.data
        if self.root.getHeight() == 0:
            self.root = None
            return returnItem
        deepestNode = self.getDeepestNode()
        self.root.data = deepestNode.data
        self._removeDeepest()
        self._reheapify(self.root)
        self.size -= 1
        return returnItem

    def _reheapify(self, currNode):
        """
        Precondition: Heap is not empty
        Postcondition: Heap root is moved to a valid position (or unchanged, if it should be the root)
        If the root is greater than its children, trickles it down until it is in a valid position
        """
        if self.isEmpty():
            return KeyError("Heap is empty")
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
        """
        Precondition: Heap is not empty
        Return: Minimum item in heap
        """
        if self.isEmpty():
            return KeyError("Heap is empty")
        return self.root.data