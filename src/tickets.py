from src.queues import Queue
from datetime import date, timedelta

class Ticket:
    def __init__(self, title, description, tasks, priority):
        self.title = title
        self.description = description
        self.tasks = Queue(tasks)
        self.leadDays = sum([task.leadDays() for task in tasks])
        self.dueDate = date.today() + timedelta(days=self.leadDays)
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
    
    def __str__(self):
        result = ""
        for task in self.tasks:
            result += str(task) + "\n"
        return result
    
    def _updateCompletionStatus(self):
        if self.getNextTask().isFinished == True:
            self.close()

    def getNextTask(self):
        return self.tasks.peek()
    
    def finishNextTask(self):
        yn = input(f"Are you sure you want to mark the following task as complete?:\n{self.getNextTask}\n")
        if yn.lower() == 'y':
            self.tasks.push(self.tasks.pop().finishTask)
            self._updateCompletionStatus()
        print("Cancelling.\n")
            
    def daysTilDue(self):
        day1 = date.strptime(date.today(), "%Y-%m-%d")
        day2 = date.strptime(self.dueDate, "%Y-%m-%d")
        return abs((day2 - day1).days)
    
    def isClosed(self):
        return self.closed
    
    def close(self):
        self.closed = True
        return self