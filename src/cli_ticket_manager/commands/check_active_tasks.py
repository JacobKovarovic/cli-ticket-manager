"""
Prints active tasks for user's current team in priority order.
If there are no active tasks, the message "No tickets found, your team is all clear!" will be displayed.
"""

from textwrap import indent
from cli_ticket_manager.classes.queue import PriorityQueue
from cli_ticket_manager.classes.user import User

def check_active_tasks(user: User, args: list[str]):
    relevantTasks = PriorityQueue()
    for ticket in user.session.tickets:
        if not ticket.isClosed():
            for task in ticket.getUnfinishedTasks():
                if task.getTeam() == user.team:
                    relevantTasks.enqueue(task)

    if relevantTasks.isEmpty():
        print("No tickets found, your team is all clear!")
    else:
        for task in relevantTasks:
            print(task.getParentTicket())
            print(indent(str(task), "\t"))