from src.queues import Queue
from datetime import date, timedelta, datetime
from src.tasks import Task

class Ticket:
    def __init__(self, title, description, tasks, priority, leadDays = None, creationDate = date.today(), closed = False):
        self.title = title
        self.description = description
        if type(tasks[0]) == list:
            tasks = [Task(*tuple(task)) for task in tasks]
        self.tasks = Queue(tasks)
        self.priority = priority
        self.creationDate = creationDate
        if type(self.creationDate) == str:
            self.creationDate = datetime.strptime(self.creationDate, '%Y, %m, %d')
        if leadDays == None:
            self.leadDays = sum([task.getLeadDays() for task in tasks])
        else:
            self.leadDays = leadDays
        self.dueDate = self.creationDate + timedelta(days=self.leadDays)
        self.closed = closed

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
               self.description == other.description and \
               self.tasks == other.tasks and \
               self.priority == other.priority and \
               self.creationDate == other.creationDate and \
               self.closed == other.closed
    
    def __str__(self):
        closed = "Yes" if self.isClosed() else "No"
        result = f"Ticket: {self.title}\n"
        result += f"{self.description}\n"
        result += f"Due Date: {self.dueDate}\n"
        result += f"Priority: {self.priority}\n"
        result += f"Closed: {closed}\n"
        result += "===================================\n"
        for task in self.tasks:
            result += str(task) + "\n"
        return result
    
    def toList(self):
        return [self.title, self.description, [task.toList() for task in self.tasks],
                self.priority, self.leadDays, self.creationDate.strftime("%Y, %m, %d"),
                self.closed]
    
    def _updateCompletionStatus(self):
        if self.getNextTask().isFinished == True:
            self.close()
            input("Final task complete! Ticket closed")

    def getNextTask(self):
        return self.tasks.peek()
    
    def getUnfinishedTasks(self):
        return [task for task in self.tasks if not task.isFinished()]
    
    def getFinishedTasks(self):
        return [task for task in self.tasks if task.isFinished()]
    
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