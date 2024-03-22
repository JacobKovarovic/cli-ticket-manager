"""
Prints all open tickets in ticket store.
Arguments:
-t, -tasks: Prints all tasks for all tickets.
-c, -closed: Print closed tickets
"""

from cli_ticket_manager.classes.user import User
from cli_ticket_manager.classes.queue import PriorityQueue

def list_tickets(user: User, args: list[str]):
    valid_arguments = ['-t', '-tasks', '-c', '-closed']
    usage = "Usage:\nlist_tickets.py\n\t-t -tasks (Print all tasks in all tickets)"
    printTasks = False
    printClosed = False

    if len(args) > 2:
        print("Too many arguments.\n" + usage)
        return
    if len(args) > 0:
        for arg in args:
            arg.rstrip()
            if arg not in valid_arguments:
                print("Invalid argument.\n" + usage)
                return
            if arg in ['-t', '-tasks']:
                printTasks = True
            if arg in ['-c', '-closed']:
                printClosed = True

    pq = PriorityQueue()
    print()
    if user.session.tickets == []:
        print("No tickets to list.")
    else:
        for ticket in user.session.tickets:
            if not printClosed:
                if ticket.isClosed():
                    continue
            pq.enqueue(ticket)
        while not pq.isEmpty():
            nextTicket = pq.dequeue()
            if printTasks:
                print(nextTicket)
            else:
                print(nextTicket.getTitle(), end = "")
                if printClosed:
                    print(" - Closed" if nextTicket.isClosed() else " - Open")
                else:
                    print()
    print()