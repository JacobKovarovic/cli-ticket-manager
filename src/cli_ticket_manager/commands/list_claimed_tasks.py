"""
Prints all tasks claimed by the user in priority order.
If no tasks have been claimed, displays the message "User has no claimed tasks."
"""

from textwrap import indent
from cli_ticket_manager.classes.user import User
from cli_ticket_manager.classes.queue import PriorityQueue

def list_claimed_tasks(user: User, args: list[str]):
    if user.session.tickets == []:
        print("No tickets.")
        return

    hasTask = False
    pq = PriorityQueue()
    for ticket in user.session.tickets:
        task = ticket.getNextTask()
        if not ticket.isClosed() and task.getOwner() == user.username:
            pq.enqueue(task)
            hasTask = True

    if not hasTask:
        print("User has no claimed tasks.")
    else:
        print()
        for task in pq:
            print(task.getParentTicket())
            print(indent(str(task), "\t"))