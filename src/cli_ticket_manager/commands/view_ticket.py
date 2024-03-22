"""
Print ticket information and full task list.
Usage: view_ticket.py "<ticketName>"
"""

import sys
from cli_ticket_manager.classes.user import User

def view_ticket(user: User, args: list[str]):
    if (len(args) != 1):
        raise ValueError('Incorrect number of arguments. Usage: view_ticket.py "<ticketName>"')

    if user.session.tickets == []:
        raise ValueError("There are no tickets.")
    key = args[0]
    print()
    for ticket in user.session.tickets:
        if ticket.getTitle() == key:
            print(ticket)
            return

    raise KeyError("No open ticket with that name found.")