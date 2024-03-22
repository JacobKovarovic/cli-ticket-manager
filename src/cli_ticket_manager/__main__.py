import sys
import os
import shlex
from .commands import *

user_commands = {
    "exit": "exit",
    "check_active_tasks": check_active_tasks,
    "claim_task": claim_task,
    "create_ticket": create_ticket,
    "finish_task": finish_task,
    "force_close_ticket": force_close_ticket,
    "list_claimed_tasks": list_claimed_tasks,
    "list_tickets": list_tickets,
    "view_ticket": view_ticket,
}

def cls(username: str = ""):
    os.system('cls' if os.name=='nt' else 'clear')
    print("Welcome to the CLI Ticket Manager", username)
    print("\"exit\" to exit")

def is_valid_selection(selection: int, highest_option: int):
    return selection in range(1, highest_option + 1)

def pause():
    input("Press Enter to continue...")

def select():
    return input("Please enter your selection: ")

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        raise ValueError("Not enough arguments. Hint: ctm login <username>")
    
    if len(args) > 3:
        raise ValueError("Too many arguments. Hint: ctm login <username>")

    if args[0] == "login":
        if len(args) < 2:
            raise ValueError("No username. Usage: ctm login <username>")
        
        username = args[1]
        user = sign_in(username)
        if user != None:
            user.log_in()
            cls(user.username)
            exiting = False
            while not exiting:
                # Split user input and preserve quoted strings
                user_input = shlex.split(input())

                if user_input == []:
                    continue
                
                cmd = user_input[0]
                cmd_args = user_input[1:]
                if cmd == "exit":
                    user.log_out()
                    return
                
                elif cmd == "cls":
                    cls(user.username)
                    continue
                
                elif cmd in user_commands.keys():
                    # Directly invoke command specified
                    try:
                        user_commands[cmd](user, cmd_args)
                    except TypeError as e:
                        print(e)
                    continue

                print("Command not found.")

    if args[0] == "register_user":
        register_user()

    # TODO: Add help docs
    
if __name__ == '__main__':
    main()