"""
Trigger a series of prompts to create a new ticket.
Precondition: User is on management team.
Postcondition: New ticket is created and stored.
"""
from sys import exit
import json
from cli_ticket_manager.classes.ticket import Ticket
from cli_ticket_manager.classes.task import Task
from cli_ticket_manager.classes.user import User

def create_ticket(user: User, args: list[str]):
    if user.team != 'management':
        print("Only managers can create tickets!")
        return

    AVAILABLE_TEAMS = ["programming", "art", "sound", "quality assurance", "management"]

    title = input("Input ticket title: ")
    if user.session.tickets != []:
        if title in [ticket.getTitle for ticket in user.session.tickets]:
            print("Cannot create duplicate ticket.")

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

    user.session.tickets.append(newTicket)
    user.session.save_tickets()
    print("New ticket has been created.")