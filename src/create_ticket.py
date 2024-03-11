"""
Trigger a series of prompts to create a new ticket.
Precondition: User is on management team.
Postcondition: New ticket is created and stored.
"""

from sys import exit
import json
from utils.tickets import Ticket
from utils.tasks import Task
from utils.user_operations import check_logged_out, get_loggedin_user, load_tickets, store_tickets

def main():
    check_logged_out()
    user = get_loggedin_user()
    allTickets = load_tickets()

    if user[1] != 'management':
        exit("Only managers can create tickets!")

    AVAILABLE_TEAMS = ["programming", "art", "sound", "quality assurance", "management"]

    title = input("Input ticket title: ")
    if allTickets != []:
        if title in [ticket.getTitle for ticket in allTickets]:
            raise ValueError("Cannot create duplicate ticket.")

    ticket_description = input("Input ticket description: ")
    tasks = []

    addTask = True
    input("Please input tasks in order of completion. At least one task must be added. Return to continue. ")
    while addTask:
        task_description = input("Please input task description: ")
        valid_team = False
        while not valid_team:
            team = input(f"Teams: {[team.title() for team in AVAILABLE_TEAMS]}\nPlease enter team responsible for task: ").lower()
            valid_team = team in AVAILABLE_TEAMS
            if not valid_team:
                print("Please choose a team from the list.")

        valid_days = False
        while not valid_days:
            try:
                leadDays = input("Please input number of days to complete task: ")
                leadDays = int(leadDays)
                valid_days = True
            except ValueError:
                print("Input must be a number.")

        valid_priority = False
        while not valid_priority:
            try:
                priority = input("Please input priority of task completion (Relative to other team tasks): ")
                priority = int(priority)
                valid_priority = True
            except ValueError:
                print("Input must be a number.")

        tasks.append(Task(task_description, team, leadDays, priority))
        
        yn = input("Add another task (y/n)? ")
        if yn != 'y':
            addTask = False

    valid_priority = False
    while not valid_priority:
        try:
            priority = input("Please input priority of ticket completion (Relative to other tickets): ")
            priority = int(priority)
            valid_priority = True
        except ValueError:
            print("Input must be a number.")

    newTicket = Ticket(title, ticket_description, tasks, priority)

    allTickets.append(newTicket)
    store_tickets(allTickets)
    print("New ticket has been created.")

if __name__ == "__main__":
    main()