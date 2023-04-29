from nodes import TreeNode

class AbstractHeap():
    def __init__(self, sourceCollection = None):
        self.size = 0
        self.head = None
        if sourceCollection != None:
            if not iter(sourceCollection):
                raise TypeError("Source collection must be iterable")
            for item in sourceCollection:
                self.add(item)

    def __str__(self):
        return str(map(str, self))

class MinHeap(AbstractHeap):
    def __init__(self, sourceCollection = None):
        super(sourceCollection)