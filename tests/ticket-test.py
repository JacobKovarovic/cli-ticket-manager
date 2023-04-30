# Set path for module imports from parent directory
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) 

from src.tasks import Task
from src.tickets import Ticket

task1 = Task("MyTask", "Art", 3, 3)
task2 = Task("MyTask2", "Programming", 3, 1)

tasks = [task1, task2]
ticket1 = Ticket("MyTicket", "My first ticket", tasks, 2)

print(ticket1)
ticket1.finishNextTask()
print(ticket1)