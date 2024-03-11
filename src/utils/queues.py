from utils.nodes import Node
from utils.heaps import MinHeap

class _AbstractQueue():
    """
    Abstract Queue class. Stores pointer to front of queue
    and queue size. Every queue subclass should have a push() and pop()
    implementation.
    """
    def __init__(self, sourceCollection = None):
        self.front = None
        self.size = 0
        if sourceCollection != None:
            for item in sourceCollection:
                self.enqueue(item)

    def __str__(self):
        """
        Return: String representation of queue.
        Front element is at the top of the list.
        """
        result = "\n"
        copyQueue = self.clone()
        while not copyQueue.isEmpty():
            result += str(copyQueue.dequeue()) + "\n"
        return result
    
    def __repr__(self):
        """
        Return: Machine readable (JSON) string representation of queue
        """
        result = []
        copyQueue = self.clone()
        while not copyQueue.isEmpty():
            result.append(copyQueue.dequeue())
        format(result)
    
    def __iter__(self):
        """
        Return iterable list of queue elements
        """
        result = []
        copyQueue = self.clone()
        while not copyQueue.isEmpty():
            result.append(copyQueue.dequeue())
        return iter(result)

    def isEmpty(self):
        """
        Return: True if queue is empty, False otherwise
        """
        return self.size == 0
    
class Queue(_AbstractQueue):
    """
    Linked queue implementation, uses linked nodes.
    The front node is the front element in the queue,
    which is chained to the each next element in the queue
    through the last element.
    """
    def __init__(self, sourceCollection = None):
        self.rear = None
        super().__init__(sourceCollection)

    def clone(self):
        """
        Return: Copy of queue
        """
        if self.isEmpty():
            return Queue()
        items = []
        probe = self.front
        while probe != None:
            items.append(probe.data)
            probe = probe.next
        return Queue(items)

    def enqueue(self, item):
        """
        Postcondition: New element is inserted at the back of the queue.
        """
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
        """
        Precondition: Queue is not empty
        Postcondition: Front element is removed from queue, next element becomes front
        Return: Value of old front element.
        """
        if self.isEmpty():
            raise KeyError("Queue is empty.")
        returnItem = self.front.data
        if self.size == 1:
            self.front = self.rear = None
            self.size -= 1
            return returnItem
        self.front = self.front.next
        self.size -= 1
        return returnItem
    
    def peek(self):
        """
        Return: Value of front element in queue.
        """
        return self.front.data

class PriorityQueue(_AbstractQueue):
    """
    Uses min heap implementation.
    Item in the queue with the smallest value is always at the front of the queue.
    """
    def __init__(self, sourceCollection = None):
        self.heap = MinHeap()
        super().__init__(sourceCollection)

    def clone(self):
        """
        Return: Copy of Priority Queue
        """
        if self.isEmpty():
            return PriorityQueue()
        return PriorityQueue([item for item in self.heap])

    def enqueue(self, item):
        """
        Postcondition: New element is placed in Priority Queue
        """
        self.heap.push(item)
        self.size += 1

    def dequeue(self):
        """
        Precondition: Priority Queue is not empty
        Postcondition: Front element is removed from Priority Queue, next smallest element becomes front
        Return: Value of old front element.
        """
        if self.isEmpty():
            raise KeyError("Queue is empty")
        self.size -= 1
        return self.heap.pop()
    
    def peek(self):
        """
        Return: Value of front element in queue
        """
        return self.heap.peek()