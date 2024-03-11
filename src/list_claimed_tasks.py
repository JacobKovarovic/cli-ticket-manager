"""
Prints all tasks claimed by the user in priority order.
If no tasks have been claimed, displays the message "User has no claimed tasks."
"""

from textwrap import indent
from utils.user_operations import check_logged_out, load_tickets, get_loggedin_user
from utils.queues import PriorityQueue

def main():
    check_logged_out()
    user = get_loggedin_user()
    allTickets = load_tickets()
    if allTickets == []:
        raise ValueError("No tickets.")

    hasTask = False
    pq = PriorityQueue()
    for ticket in allTickets:
        task = ticket.getNextTask()
        if not ticket.isClosed() and task.getOwner() == user[0]:
            pq.enqueue(task)
            hasTask = True

    if not hasTask:
        print("User has no claimed tasks.")
    else:
        print()
        for task in pq:
            print(task.getParentTicket())
            print(indent(str(task), "\t"))

if __name__ == "__main__":
    main()