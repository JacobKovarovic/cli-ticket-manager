"""
Prints active tasks for user's current team in priority order.
If there are no active tasks, the message "No tickets found, your team is all clear!" will be displayed.
"""

from textwrap import indent
from src.queues import PriorityQueue
from src.user_operations import load_tickets, check_logged_out, get_loggedin_user

def main():
    check_logged_out()
    user = get_loggedin_user()
    allTickets = load_tickets()

    relevantTasks = PriorityQueue()
    for ticket in allTickets:
        if not ticket.isClosed():
            for task in ticket.getUnfinishedTasks():
                if task.getTeam() == user[1]:
                    relevantTasks.enqueue(task)

    if relevantTasks.isEmpty():
        print("No tickets found, your team is all clear!")
    else:
        for task in relevantTasks:
            print(task.getParentTicket())
            print(indent(str(task), "\t"))

if __name__ == "__main__":
    main()