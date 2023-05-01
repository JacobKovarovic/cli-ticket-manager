from datetime import date, timedelta, datetime

class Task():
    """
    Task class.
    Stores information about a team task.
    Comparisons based on priority for insertion into priority queues.
    """

    AVAILABLE_TEAMS = ["programming", "art", "sound", "quality assurance", "management"]

    def __init__(self, description, team, leadDays, priority, dateCreated = date.today(), claimedBy = None, finished = False):
        if team not in Task.AVAILABLE_TEAMS:
            raise ValueError(f"Invalid team: {team}\n \
                             Please assign each task to one of the following teams: \
                             {Task.AVAILABLE_TEAMS}")
        self.description = description
        self.team = team
        self.dateCreated = dateCreated
        if type(self.dateCreated) == str:
            self.dateCreated = datetime.strptime(self.dateCreated, '%Y, %m, %d').date()
        self.leadDays = leadDays
        self.dueDate = self.dateCreated + timedelta(days=self.leadDays)
        self.priority = priority
        self.claimedBy = claimedBy
        self.parentTicket = None
        self.finished = finished

    def __lt__(self, other):
        """
        Return: True if priority of self is less than other task.
        """
        if type(other) != type(self):
            raise TypeError("Only Tasks can be compared to Tasks")
        return self.priority < other.priority
    
    def __gt__(self, other):
        """
        Return: True if priority of self is greater than other task.
        """
        if type(other) != type(self):
            raise TypeError("Only Tasks can be compared to Tasks")
        return self.priority > other.priority
    
    def __eq__(self, other):
        """
        Compares equality of tickets based on:
        Description, team, date created, lead days,
        ownership, priority, and finished status
        """
        if type(other) != type(self):
            raise TypeError("Only Tasks can be compared to Tasks")
        return self.description == other.description and \
               self.team == other.team and \
               self.dateCreated == other.dateCreated and \
               self.leadDays == other.leadDays and \
               self.claimedBy == other.claimedBy and \
               self.priority == other.priority and \
               self.finished == other.finished
    
    def __str__(self):
        """
        Return: string representation of task data.
        """
        complete = "Yes" if self.isFinished() else "No"
        s = f"{type(self).__name__}: {self.description}\n"
        s += f"Team: {self.team}\n"
        s += f"Due Date: {self.dueDate}\n"
        s += f"Priority: {self.priority}\n"
        s += f"Complete: {complete}\n"
        s += f"Claimed By: {self.claimedBy}\n"
        return s
    
    def toList(self):
        """
        Return: list representation of task data.
        """
        return [self.description, self.team, self.leadDays,
                self.priority, self.dateCreated.strftime("%Y, %m, %d"), self.claimedBy,
                self.finished]
    
    def daysTilDue(self):
        """
        Return: Days remaining from today until task due date.
        """
        day1 = date.today().strftime("%Y, %m, %d")
        day2 = self.dueDate.strftime("%Y, %m, %d")
        return abs((day2 - day1).days)
    
    def getLeadDays(self):
        """
        Return: Task lead days.
        """
        return self.leadDays
    
    def getTeam(self):
        """
        Return: Task assigned team.
        """
        return self.team
    
    def isFinished(self):
        """
        Return: True if task is finished, False otherwise.
        """
        return self.finished
    
    def setParentTicket(self, ticketName):
        """
        Postcondition: Task parent ticket value is set to ticketName
        """
        self.parentTicket = ticketName

    def getParentTicket(self):
        """
        Return: Name of parent ticket
        """
        return self.parentTicket
    
    def setOwner(self, username):
        """
        Postcondition: Set owner of ticket to username
        """
        self.claimedBy = username
    
    def getOwner(self):
        """
        Return: Owner of ticket
        """
        return self.claimedBy
    
    def finishTask(self):
        """
        Postcondition: Status of task is set to finished
        """
        self.finished = True
        return self