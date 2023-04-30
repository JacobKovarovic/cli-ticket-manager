from src.queues import Queue
from datetime import date

class Ticket:
    def __init__(self, title, description, tasks, priority):
        self.title = title
        self.description = description
        self.tasks = Queue(tasks)
        self.priority = priority
        self.creationDate = date.today()
        self.closed = False

    def __lt__(self, other):
        return 

    def isClosed(self):
        return not self.closed