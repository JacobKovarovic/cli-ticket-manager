import sys
from src.user_operations import check_logged_out, load_tickets, store_tickets, get_loggedin_user

check_logged_out()
user = get_loggedin_user()
if (len(sys.argv) != 2):
    raise ValueError('Incorrect number of arguments: Usage "finish_task.py "<ticketName>"')

allTickets = load_tickets()
if allTickets == []:
    raise ValueError("There are no tickets.")
key = sys.argv[1]
for ticket in allTickets:
    if not ticket.isClosed() and ticket.getTitle() == key:
        task = ticket.getNextTask()
        print(f"\n{ticket.getTitle()}")
        print("====================")
        print(task)
        if task.getTeam() != user[1]:
            raise ValueError("Next task on this ticket is for a different team.")
        if task.getOwner() != user[0]:
            raise ValueError("You have not claimed this task. Use claim_task.py first.")
        yn = input("Are you sure you want to finish this task (y/n)? ").lower()
        if yn != 'y':
            sys.exit("Cancelling.")
        else:
            ticket.finishNextTask()
            store_tickets(allTickets)
            sys.exit("Task marked as finished.")

raise KeyError("No open ticket with that name found.")