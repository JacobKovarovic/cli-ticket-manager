from src.user_operations import check_logged_out, load_tickets
from src.queues import PriorityQueue
import sys

check_logged_out()
usage = "Usage:\nlist_tickets.py\n\t-t -tasks (Print all tasks in all tickets)"
printTasks = False

if len(sys.argv) > 2:
    raise KeyError("Too many arguments.\n" + usage)
if len(sys.argv) > 1:
    if sys.argv[1].rstrip() not in ['-t', '-tasks']:
        raise ValueError("Invalid argument.\n" + usage)
    else:
        printTasks = True

allTickets = load_tickets()
pq = PriorityQueue()
print()
if allTickets == []:
    print("No tickets to list.")
else:
    for ticket in allTickets:
        pq.enqueue(ticket)
    while not pq.isEmpty():
        if printTasks:
            print(pq.dequeue())
        else:
            print(pq.dequeue().getTitle())