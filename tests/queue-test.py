# Set path for module imports from parent directory
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) 

from src.queues import Queue, PriorityQueue

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