from src.user_operations import check_logged_out, load_tickets
from src.queues import PriorityQueue

check_logged_out()
allTickets = load_tickets()
pq = PriorityQueue()
print()
if allTickets == []:
    print("No tickets to list.")
else:
    for ticket in allTickets:
        pq.enqueue(ticket)
    while not pq.isEmpty():
        print(pq.dequeue())