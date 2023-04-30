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
        if type(other) != type(self):
            raise TypeError("Only Tickets can be compared to Tickets")
        return self.priority < other.priority
    
    def __gt__(self, other):
        if type(other) != type(self):
            raise TypeError("Only Tickets can be compared to Tickets")
        return self.priority > other.priority
    
    def __eq__(self, other):
        if type(other) != type(self):
            raise TypeError("Only Tickets can be compared to Tickets")
        return self.title == other.title and \
               self.descriptio == other.description and \
               self.tasks == other.tasks and \
               self.priority == other.priority and \
               self.creationDate == other.creationDate and \
               self.closed == other.closed
    
    def isClosed(self):
        return not self.closed