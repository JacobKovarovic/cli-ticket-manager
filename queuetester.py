from queues import Queue, PriorityQueue

q = Queue()
pq = PriorityQueue()
for i in reversed(range(10)):
    q.enqueue(i)
    pq.enqueue(i)

print("Front:", q.peek())
print(q)

print("Front:", pq.peek())
print(pq)