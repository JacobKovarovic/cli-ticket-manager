from src.queues import Queue
from datetime import date, timedelta, datetime
from src.tasks import Task

class Ticket:
    """
    Ticket class.
    Stores information about a project ticket.
    Comparisons based on priority for insertion into priority queues.
    Tasks are stored in a queue in the order they must be completed in.
    When a task is finished, it is placed onto the back of the
    queue, so that when the front task in the queue is finished, it means that
    every task has been completed.
    """
    def __init__(self, title, description, tasks, priority, leadDays = None, creationDate = date.today(), closed = False):
        self.title = title
        self.description = description
        if type(tasks[0]) == list:
            tasks = [Task(*tuple(task)) for task in tasks]
        for task in tasks:
            task.setParentTicket(self.title)
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
        """
        Return: True if self priority is less than other priority
        """
        if type(other) != type(self):
            raise TypeError("Only Tickets can be compared to Tickets")
        return self.priority < other.priority
    
    def __gt__(self, other):
        """
        Return: True if self priority is greater than other priority
        """
        if type(other) != type(self):
            raise TypeError("Only Tickets can be compared to Tickets")
        return self.priority > other.priority
    
    def __eq__(self, other):
        """
        Compare self to other based on:
        Title, description, tasks, priority,
        creation date, and closed status
        """
        if type(other) != type(self):
            raise TypeError("Only Tickets can be compared to Tickets")
        return self.title == other.title and \
               self.description == other.description and \
               self.tasks == other.tasks and \
               self.priority == other.priority and \
               self.creationDate == other.creationDate and \
               self.closed == other.closed
    
    def __str__(self):
        """
        Return: String representation of ticket.
        """
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
        """
        Return: List representation of ticket
        """
        return [self.title, self.description, [task.toList() for task in self.tasks],
                self.priority, self.leadDays, self.creationDate.strftime("%Y, %m, %d"),
                self.closed]
    
    def _updateCompletionStatus(self):
        """
        Precondition: All tasks in a ticket are finished
        Postcondition: Ticket is set to closed
        """
        if self.getNextTask().isFinished == True:
            self.close()
            input("Final task complete! Ticket closed")

    def getTitle(self):
        """
        Return: Title of ticket
        """
        return self.title

    def getNextTask(self):
        """
        Return: Next task in ticket task queue
        """
        return self.tasks.peek()
    
    def getUnfinishedTasks(self):
        """
        Return: All unfinished tasks in ticket queue in completion order
        """
        return [task for task in self.tasks if not task.isFinished()]
    
    def getFinishedTasks(self):
        """
        Return: All unfinished tasks in ticket queue in completed order.
        """
        return [task for task in self.tasks if task.isFinished()]
    
    def finishNextTask(self):
        """
        Postcondition: Mark next task as finished, and place it in the back of the tasks queue.
        """
        finishedTask = self.tasks.dequeue()
        finishedTask.finishTask()
        self.tasks.enqueue(finishedTask)
        self._updateCompletionStatus()
            
    def daysTilDue(self):
        """
        Return: Days until ticket due date from today
        """
        day1 = date.strptime(date.today(), "%Y-%m-%d")
        day2 = date.strptime(self.dueDate, "%Y-%m-%d")
        return abs((day2 - day1).days)
    
    def isClosed(self):
        """
        Return: True if ticket is closed, false otherwise.
        """
        return self.closed
    
    def close(self):
        """
        Postcondition: Close ticket.
        """
        self.closed = True
        return self