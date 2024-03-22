"""
Usage: finish_task.py "<ticketName>"
Precondition: Next task in given ticket is claimed by user
Postcondition: Set task to finished, ticket store updated
"""
from cli_ticket_manager.classes.user import User

def finish_task(user: User, args: list[str]):
    if (len(args) != 1):
        raise TypeError('Incorrect number of arguments: Usage "finish_task.py "<ticketName>"')

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
            if task.getOwner() != user.username:
                print("You have not claimed this task. Use claim_task.py first.")
                return
            yn = input("Are you sure you want to finish this task (y/n)? ").lower()
            if yn != 'y':
                print("Cancelling.")
                return
            else:
                ticket.finishNextTask()
                user.session.save_tickets()
                print("Task marked as finished.")
                return

    print("No open ticket with that name found.")