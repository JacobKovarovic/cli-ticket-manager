import json
import re

AVAILABLE_TEAMS = ["programming", "art", "sound", "quality assurance", "management"]
validUsername = False
validTeam = False

while not validUsername:
    username = input("Please input new user's username: ")
    validUsername = re.search("^[a-z0-9_-]{3,15}$", username) == None
    if not validUsername:
        print("Username must be 3-15 alphanumeric characters.")

while not validTeam:
    print("\nTeams:", [item.title() for item in AVAILABLE_TEAMS])
    team = input("Please input new user's team: ")
    validTeam = team.lower() in AVAILABLE_TEAMS
    if not validTeam:
        print("User must be in one of the teams listed.")

usersFile = open('users.json', 'r')
fileContents = usersFile.readline()
if fileContents != '':
    users = json.loads(fileContents)
else:
    users = []
usersFile.close()

users.append([username, team])

usersFile = open('users.json', 'w')
usersFile.write(json.dumps(users))
usersFile.close()
print(f"User {username} on team {team.capitalize()} registered.")