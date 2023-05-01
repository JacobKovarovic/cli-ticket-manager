from textwrap import indent
from src.user_operations import check_logged_out, load_tickets, get_loggedin_user

check_logged_out()
user = get_loggedin_user()
allTickets = load_tickets()
if allTickets == []:
    raise ValueError("No tickets.")

hasTask = False
for ticket in allTickets:
    if not ticket.isClosed() and ticket.getNextTask().getOwner() == user[0]:
        task = ticket.getNextTask()
        print(task.getParentTicket())
        print(indent(str(task), "\t"))
        hasTask = True

if not hasTask:
    print("User has no claimed tasks.")