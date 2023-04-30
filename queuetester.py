from queues import Queue

q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print("Front:", q.peek())
print(q)