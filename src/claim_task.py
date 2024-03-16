"""
Usage: check_active_tasks.py "<ticketName>"
Precondition: Next task in given ticket is available to user's team and not claimed
Postcondition: Set task to claimed by user if task is not claimed, ticket store updated
"""

import sys
from utils.user_operations import check_logged_out, load_tickets, store_tickets, get_loggedin_user

def main():
    check_logged_out()
    user = get_loggedin_user()
    if (len(sys.argv) != 2):
        raise ValueError('Incorrect number of arguments. Usage: check_active_tasks.py "<ticketName>"')

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
            if task.getOwner() != None:
                raise ValueError("Task has been claimed by another user.")
            yn = input("Are you sure you want to claim this task (y/n)? ").lower()
            if yn != 'y':
                sys.exit("Cancelling.")
            else:
                ticket.getNextTask().setOwner(user[0])
                print(ticket.getNextTask())
                store_tickets(allTickets)
                sys.exit("Task claimed.")

    raise KeyError("No open ticket with that name found.")

if __name__ == "__main__":
    main()