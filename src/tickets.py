from src.queues import Queue
from datetime import date, timedelta

class Ticket:
    def __init__(self, title, description, tasks, priority):
        self.title = title
        self.description = description
        self.tasks = Queue(tasks)
        self.leadDays = sum([task.getLeadDays() for task in tasks])
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
        closed = "Yes" if self.isClosed() else "No"
        result = f"Ticket: {self.title}\n"
        result += f"{self.description}\n\n"
        result += f"Due Date: {self.dueDate}\n"
        result += f"Priority: {self.priority}\n"
        result += f"Closed: {closed}\n"
        result += "===================================\n"
        for task in self.tasks:
            result += str(task) + "\n"
        return result
    
    def _updateCompletionStatus(self):
        if self.getNextTask().isFinished == True:
            self.close()
            input("Final task complete! Ticket closed")

    def getNextTask(self):
        return self.tasks.peek()
    
    def finishNextTask(self):
        yn = input(f"Are you sure you want to mark the following task as complete?:\n{self.getNextTask()}\n(y/n): ")
        if yn.lower() == 'y':
            finishedTask = self.tasks.dequeue()
            finishedTask.finishTask()
            self.tasks.enqueue(finishedTask)
            input("Task marked complete. Return to continue")
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