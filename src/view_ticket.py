"""
Print ticket information and full task list.
Usage: view_ticket.py "<ticketName>"
"""

import sys
from utils.user_operations import check_logged_out, load_tickets

def main():
    check_logged_out()
    if (len(sys.argv) != 2):
        raise ValueError('Incorrect number of arguments. Usage: view_ticket.py "<ticketName>"')

    allTickets = load_tickets()
    if allTickets == []:
        raise ValueError("There are no tickets.")
    key = sys.argv[1]
    print()
    for ticket in allTickets:
        if ticket.getTitle() == key:
            print(ticket)
            sys.exit()

    raise KeyError("No open ticket with that name found.")

if __name__ == "__main__":
    main()