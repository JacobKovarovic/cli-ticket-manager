import json
from sys import exit

session = open("session.json", 'r')
if session.readline() != '':
    session.close()
    usersFile = open('users.json', 'r')
    fileContents = usersFile.readline()
    if fileContents == '':
        raise ValueError("There are no users!")
    users = json.loads(fileContents)
    usersFile.close()

    validUsername = False
    while not validUsername:
        username = input("Please input your username (Return to exit): ")
        if username == '':
            exit("Login cancelled")
        if username not in [user[0] for user in users]:
            print("User not found.")
        else:
            validUsername = True

    session = open('session.json', 'w')
    session.write(json.dumps([user for user in users if user[0] == username][0]))
else:
    print("User is already signed in. Please sign out to sign in as other user.")

session.close()