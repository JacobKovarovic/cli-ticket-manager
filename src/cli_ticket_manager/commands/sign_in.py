import json
from cli_ticket_manager.classes.user import User
"""
Sign user in.
Precondition: Username must exist in users store.
Return: User object if user successfully logged in, None otherwise
"""

def sign_in(username: str) -> User:
    usersFile = open('data/users.json', 'r')
    fileContents = usersFile.readline()
    if fileContents == '':
        raise ValueError("There are no registered users!")
    users = json.loads(fileContents)
    usersFile.close()

    for user in users:
        if username == user[0]:
            return User(user[0], user[1])
            
    print("User not found.")

    return None