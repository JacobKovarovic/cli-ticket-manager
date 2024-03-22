"""
Usage: force_close_ticket.py "<ticketName>"
Precondition: Given ticket exists and is not already closed.
Postcondition: Given ticket is closed.
"""
import sys
from cli_ticket_manager.classes.user import User

def force_close_ticket(user: User, args: list[str]):
    if user.team != "management":
        print('Only managers can force close tickets!')
        return
    if (len(args) != 1):
        print('Incorrect number of arguments: Usage "force_close_ticket.py "<ticketName>"')
        return

    if user.session.tickets == []:
        print("There are no tickets.")
        return
    
    key = args[0]
    print()
    for ticket in user.session.tickets:
        if not ticket.isClosed() and ticket.getTitle() == key:
            print(ticket)
            yn = input("Are you sure you want to close this ticket before all tasks are completed (y/n)? ").lower()
            if yn != 'y':
                print("Cancelling.")
                return
            else:
                ticket.close()
                user.session.save_tickets()
                print("Ticket closed.")
                return

    print("No open ticket with that name found.")