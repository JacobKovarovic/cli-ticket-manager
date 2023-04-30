from src.tasks import Task
from src.queues import PriorityQueue

t = Task("MyTask", "Art", 3, 3)
t2 = Task("MyTask2", "Programming", 3, 1)
pq = PriorityQueue()
pq.enqueue(t)
pq.enqueue(t2)

print(t)
print(pq)