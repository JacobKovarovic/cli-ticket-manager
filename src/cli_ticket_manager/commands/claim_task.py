"""
Usage: check_active_tasks.py "<ticketName>"
Precondition: Next task in given ticket is available to user's team and not claimed
Postcondition: Set task to claimed by user if task is not claimed, ticket store updated
"""
import sys
from cli_ticket_manager.classes.user import User

def claim_task(user: User, args: list[str]):
    if (len(args) != 1):
        print('Incorrect number of arguments. Usage: claim_task "<ticketName>"')
        return

    if user.session.tickets == []:
        print("There are no tickets.")
        return
    
    key = args[0]
    for ticket in user.session.tickets:
        if not ticket.isClosed() and ticket.getTitle() == key:
            task = ticket.getNextTask()
            print(f"\n{ticket.getTitle()}")
            print("====================")
            print(task)
            if task.getTeam() != user.team:
                print("Next task on this ticket is for a different team.")
                return
            if task.getOwner() != None:
                print("Task has been claimed by another user.")
                return
            yn = input("Are you sure you want to claim this task (y/n)? ").lower()
            if yn != 'y':
                print("Cancelling.")
                return
            else:
                ticket.getNextTask().setOwner(user.username)
                print(ticket.getNextTask())
                user.session.save_tickets()
                print("Task claimed.")

    print("No open ticket with that name found.")