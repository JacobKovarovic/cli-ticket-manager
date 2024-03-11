"""
Prints all open tickets in ticket store.
Arguments:
-t, -tasks: Prints all tasks for all tickets.
-c, -closed: Print closed tickets
"""

from utils.user_operations import check_logged_out, load_tickets
from utils.queue import PriorityQueue
import sys

def main():
    check_logged_out()
    valid_arguments = ['-t', '-tasks', '-c', '-closed']
    usage = "Usage:\nlist_tickets.py\n\t-t -tasks (Print all tasks in all tickets)"
    printTasks = False
    printClosed = False

    if len(sys.argv) > 3:
        raise KeyError("Too many arguments.\n" + usage)
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            arg.rstrip()
            if arg not in valid_arguments:
                raise ValueError("Invalid argument.\n" + usage)
            if arg in ['-t', '-tasks']:
                printTasks = True
            if arg in ['-c', '-closed']:
                printClosed = True

    allTickets = load_tickets()
    pq = PriorityQueue()
    print()
    if allTickets == []:
        print("No tickets to list.")
    else:
        for ticket in allTickets:
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

if __name__ == "__main__":
    main()