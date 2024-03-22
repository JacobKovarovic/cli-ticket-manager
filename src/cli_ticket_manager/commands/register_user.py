"""
Add new user to users store.
Username must be 3-15 alphanumeric characters (underscores and hyphens allowed).
Username must not be taken.
User must be placed on one of the following teams:
Programming | Art | Sound | Quality Assurance | Management
"""

import json
import re

def register_user():
    AVAILABLE_TEAMS = ["programming", "art", "sound", "quality assurance", "management"]
    validUsername = False
    validTeam = False

    usersFile = open('data/users.json', 'r+')
    fileContents = usersFile.readline()
    if fileContents != '':
        users = json.loads(fileContents)
    else:
        users = []
    usersFile.close()

    while not validUsername:
        username = input("Please input new user's username: ")
        if users != []:
            if username in [user.username for user in users]:
                print("Username taken.")
                continue
        validUsername = re.search("^[a-zA-Z0-9_-]{3,15}$", username) is not None
        if not validUsername:
            print("Username must be 3-15 alphanumeric characters (underscores and hyphens allowed). ")

    while not validTeam:
        print("\nTeams:", [item.title() for item in AVAILABLE_TEAMS])
        team = input("Please input new user's team: ").lower()
        validTeam = team in AVAILABLE_TEAMS
        if not validTeam:
            print("User must be in one of the teams listed.")

    users.append([username, team])

    usersFile = open('data/users.json', 'w')
    usersFile.write(json.dumps(users))
    usersFile.close()
    print(f"User {username} on team {team.capitalize()} registered.")