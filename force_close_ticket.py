"""
Usage: force_close_ticket.py "<ticketName>"
Precondition: Given ticket exists and is not already closed.
Postcondition: Given ticket is closed.
"""

import sys
from src.user_operations import check_logged_out, load_tickets, store_tickets, get_loggedin_user

def main():
    check_logged_out()
    user = get_loggedin_user()
    if user[1] != "management":
        raise ValueError('Only managers can force close tickets!')
    if (len(sys.argv) != 2):
        raise ValueError('Incorrect number of arguments: Usage "force_close_ticket.py "<ticketName>"')

    allTickets = load_tickets()
    if allTickets == []:
        raise ValueError("There are no tickets.")
    key = sys.argv[1]
    print()
    for ticket in allTickets:
        if not ticket.isClosed() and ticket.getTitle() == key:
            print(ticket)
            yn = input("Are you sure you want to close this ticket before all tasks are completed (y/n)? ").lower()
            if yn != 'y':
                sys.exit("Cancelling.")
            else:
                ticket.close()
                store_tickets(allTickets)
                sys.exit("Ticket closed.")

    raise KeyError("No open ticket with that name found.")

if __name__ == "__main__":
    main()