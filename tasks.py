from queues import Queue
from datetime import date, timedelta

class Task():

    AVAILABLE_TEAMS = ["Programming", "Art", "Sound", "QA", "Management"]

    def __init__(self, description, team, leadDays, priority):
        if team not in Task.AVAILABLE_TEAMS:
            raise ValueError(f"Invalid team: {team}\n \
                             Please assign each task to one of the following teams: \
                             {Task.AVAILABLE_TEAMS}")
        self.description = description
        self.team = team
        self.creationDate = date.today()
        self.dueDate = date.today() + timedelta(days=leadDays)
        self.priority = priority

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
        return self == other
    
    def __str__(self):
        s = f"{type(self).__name__}: {self.description}\n"
        s += f"Team: {self.team}\n"
        s += f"Due Date: {self.dueDate}\n"
        s += f"Priority: {self.priority}\n"
        return s
    
    def daysTilDue(self):
        day1 = date.strptime(date.today(), "%Y-%m-%d")
        day2 = date.strptime(self.dueDate, "%Y-%m-%d")
        return abs((day2 - day1).days)
    
    def getTeam(self):
        return self.team