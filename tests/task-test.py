# Set path for module imports from parent directory
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) 
from src.tasks import Task
from src.queues import PriorityQueue

def main():
    t = Task("MyTask", "Art", 3, 3)
    t2 = Task("MyTask2", "Programming", 3, 1)
    pq = PriorityQueue()
    pq.enqueue(t)
    pq.enqueue(t2)

    print(t)
    print(pq)

if __name__ == "__main__":
    main()