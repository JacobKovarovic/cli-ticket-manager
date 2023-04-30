from queues import Queue, PriorityQueue

q = Queue()
pq = PriorityQueue()
pqClone = pq.clone()
pqClone.enqueue(5)
for i in reversed(range(10)):
    q.enqueue(i)
    pq.enqueue(i)

print("Front:", q.peek())
print(q)

print("Front:", pq.peek())
print(pq)

print("Front:", pqClone.peek())
print(pqClone)

pqClone = pq.clone()
print("Front:", pqClone.peek())
print(pqClone)