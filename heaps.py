
class AbstractHeap():
    __init__(self, sourceCollection = None):
        self.size = 0
        if sourceCollection != None:
            if not iter(sourceCollection):
                raise TypeError("Source collection must be iterable")
            for item in sourceCollection:
                self.add()

    __str__(self):
        return str(map(str, self))

    __add__(self, item):
        self.push(item)
