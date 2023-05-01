from datetime import date, timedelta, datetime

class Task():

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
        if type(other) != type(self):
            raise TypeError("Only Tasks can be compared to Tasks")
        return self.priority < other.priority
    
    def __gt__(self, other):
        if type(other) != type(self):
            raise TypeError("Only Tasks can be compared to Tasks")
        return self.priority > other.priority
    
    def __eq__(self, other):
        if type(other) != type(self):
            raise TypeError("Only Tasks can be compared to Tasks")
        return self.description == other.description and \
               self.team == other.team and \
               self.dateCreated == other.dateCreated and \
               self.leadDays == other.leadDays and \
               self.priority == other.priority and \
               self.finished == other.finished
    
    def __str__(self):
        complete = "Yes" if self.isFinished() else "No"
        s = f"{type(self).__name__}: {self.description}\n"
        s += f"Team: {self.team}\n"
        s += f"Due Date: {self.dueDate}\n"
        s += f"Priority: {self.priority}\n"
        s += f"Complete: {complete}\n"
        return s
    
    def toList(self):
        return [self.description, self.team, self.leadDays,
                self.priority, self.dateCreated.strftime("%Y, %m, %d"), self.claimedBy,
                self.finished]
    
    def daysTilDue(self):
        day1 = date.today().strftime("%Y, %m, %d")
        day2 = self.dueDate.strftime("%Y, %m, %d")
        return abs((day2 - day1).days)
    
    def getLeadDays(self):
        return self.leadDays
    
    def getTeam(self):
        return self.team
    
    def isFinished(self):
        return self.finished
    
    def setParentTicket(self, ticketName):
        self.parentTicket = ticketName

    def getParentTicket(self):
        return self.parentTicket
    
    def setOwner(self, username):
        self.claimedBy = username
    
    def getOwner(self):
        return self.claimedBy
    
    def finishTask(self):
        self.finished = True
        return self