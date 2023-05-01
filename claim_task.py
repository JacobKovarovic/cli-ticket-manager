"""
Precondition: Next task in ticket is available to user's team and not claimed
Postcondition: Set task to claimed by user if task is not claimed
"""

import sys
from src.user_operations import check_logged_out, load_tickets, get_loggedin_user

check_logged_out()
user = get_loggedin_user()
if (len(sys.argv) != 2):
    raise ValueError('Incorrect number of arguments: Usage "check_active_tasks.py "<ticketName>"')

allTickets = load_tickets()
key = sys.argv[1]
for ticket in allTickets:
    if not ticket.isClosed() and ticket.getTitle() == key:
        task = ticket.getNextTask()
        print(f"\n{ticket.getTitle()}")
        print("====================")
        print(ticket.getNextTask())
        if task.getTeam() != user[1]:
            raise ValueError("Next task on this ticket is for a different team.")
        if task.getOwner() != None:
            raise ValueError("Task has been claimed by another user.")
        yn = input("Are you sure you want to claim this task (y/n)? ").lower()
        if yn != 'y':
            exit(sys.exit("Cancelling."))
        else:
            task.setOwner(user[0])
            print(task)
            print("Task claimed.")

    else:
        raise KeyError("No open ticket with that name found.")