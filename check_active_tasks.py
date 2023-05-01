from src.queues import PriorityQueue
from src.user_operations import load_tickets, check_logged_out, get_loggedin_user

check_logged_out()
user = get_loggedin_user()
allTickets = load_tickets()

relevantTickets = PriorityQueue()
for ticket in allTickets:
    for task in ticket.getUnfinishedTasks():
        if task.getTeam() == user[1]:
            relevantTickets.enqueue(task)

if relevantTickets.isEmpty():
    print("No tickets, your team is all clear!")
else:
    print(relevantTickets)