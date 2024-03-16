class Node():
    """
    Node class for linked structures.
    Each node has a data pointer and a next pointer
    to store a reference to next node in chain.
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class TreeNode():
    """
    TreeNode class for binary tree data structures.
    Each node has a data pointer and a pointer to a left
    child node and right child node.
    """
    def __init__(self, data, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getHeight(self):
        """
        Return number of edges between root and deepest leaf.
        """
        return self._getHeight(self)
    
    def _getHeight(self, currNode):
        """
        Helper function for self.getHeight()
        Recursively finds number of edges between root and deepest leaf.
        """
        if currNode == None or (currNode.leftChild == None and currNode.rightChild == None):
            return 0
        leftHeight = self._getHeight(currNode.leftChild)
        rightHeight = self._getHeight(currNode.rightChild)
        if leftHeight > rightHeight:
            return 1 + leftHeight
        return 1 + rightHeight

    def clone(self):
        """
        Return: Copy of tree
        """
        return TreeNode(self.data, self.leftChild, self.rightChild)
    
    def __str__(self):
        """
        Return string representation of tree with node children
        in nested parenthesis.
        """
        return str(self.data) + "(" + str(self.leftChild) + ", " + str(self.rightChild) + ")"
    
    def isComplete(self):
        """
        Return: True if tree is complete. False if it is not
        """
        if self.getHeight() == 0:
            return True
        if self.leftChild == None:
            return False
        if self.rightChild == None:
            return False
        if self.leftChild.getHeight() == self.rightChild.getHeight():
            return True and self.leftChild.isComplete() and self.rightChild.isComplete()
        return False
    
    def printLikeTree(self):
        """
        Return: String representation of tree that visually resembles a tree.
        """
        def inorder(currNode, depth):
            dataHeight = [[currNode.data, depth]]
            depth += 1
            if currNode.leftChild == None and currNode.rightChild == None:
                return dataHeight
            if currNode.rightChild == None:
                return dataHeight + inorder(currNode.leftChild, depth)
            if currNode.leftChild == None:
                return dataHeight + inorder(currNode.rightChild, depth)
            return dataHeight + inorder(currNode.leftChild, depth) + inorder(currNode.rightChild, depth)
        dataAndDepths = inorder(self, 0)
        print(dataAndDepths)
        rootHeight = self.getHeight()
        for i in range(self.getHeight() + 1):
            spacesBetweenItems = pow(2, rootHeight - i)
            for item in [item[0] for item in dataAndDepths if item[1] == i]:
                print(" " * (5 * spacesBetweenItems - 1), end="")
                print(item, end="")
                print(" " * (5 * spacesBetweenItems - 1), end="")
            print()
