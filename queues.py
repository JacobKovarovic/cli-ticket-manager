from nodes import Node
from heaps import MinHeap

class _AbstractQueue():
    def __init__(self, sourceCollection = None):
        self.front = None
        self.size = 0
        if sourceCollection != None:
            for item in sourceCollection:
                self.enqueue(item)

    def __str__(self):
        result = "Front | "
        copyQueue = self.clone()
        while not copyQueue.isEmpty():
            result += str(copyQueue.dequeue()) + " | "
        result += "Rear"
        return result

    def isEmpty(self):
        return self.size == 0
    
class Queue(_AbstractQueue):
    def __init__(self, sourceCollection = None):
        self.rear = None
        super().__init__(sourceCollection)

    def clone(self):
        items = []
        probe = self.front
        while probe != None:
            items.append(probe.data)
            probe = probe.next
        return Queue(items)

    def enqueue(self, item):
        newNode = Node(item)
        if self.isEmpty():
           self.front = newNode
           self.rear = self.front
           self.size += 1
           return
        if self.size == 1:
            self.front.next = newNode
            self.rear = self.front.next
            self.size += 1
            return
        self.rear.next = newNode
        self.rear = self.rear.next
        self.size += 1

    def dequeue(self):
        returnItem = self.front.data
        if self.size == 1:
            self.front = self.rear = None
            self.size -= 1
            return returnItem
        self.front = self.front.next
        self.size -= 1
        return returnItem
    
    def peek(self):
        return self.front.data
"""
class PriorityQueue():
    def __init__(self, sourceCollection = None)
        self.items = MinHeap()
        super().__init__(sourceCollection)
    def enqueue(self, item):
        

    def dequeue(self):
"""