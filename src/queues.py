from src.nodes import Node
from src.heaps import MinHeap

class _AbstractQueue():
    def __init__(self, sourceCollection = None):
        self.front = None
        self.size = 0
        if sourceCollection != None:
            for item in sourceCollection:
                self.enqueue(item)

    def __str__(self):
        result = "\n"
        copyQueue = self.clone()
        while not copyQueue.isEmpty():
            result += str(copyQueue.dequeue()) + "\n"
        return result
    
    def __repr__(self):
        result = []
        copyQueue = self.clone()
        while not copyQueue.isEmpty():
            result.append(copyQueue.dequeue())
        format(result)
    
    def __iter__(self):
        result = []
        copyQueue = self.clone()
        while not copyQueue.isEmpty():
            result.append(copyQueue.dequeue())
        return iter(result)

    def isEmpty(self):
        return self.size == 0
    
class Queue(_AbstractQueue):
    def __init__(self, sourceCollection = None):
        self.rear = None
        super().__init__(sourceCollection)

    def clone(self):
        if self.isEmpty():
            return Queue()
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

class PriorityQueue(_AbstractQueue):
    def __init__(self, sourceCollection = None):
        self.heap = MinHeap()
        super().__init__(sourceCollection)

    def clone(self):
        if self.isEmpty():
            return PriorityQueue()
        return PriorityQueue([item for item in self.heap])

    def enqueue(self, item):
        self.heap.push(item)
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise KeyError("Queue is empty")
        self.size -= 1
        return self.heap.pop()
    
    def peek(self):
        return self.heap.peek()