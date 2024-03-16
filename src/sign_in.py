import json
"""
Sign user in.
Precondition: Username must exist in users store.
Postcondition: Session file contains signed-in user username and team for other scripts to use
"""

from utils.user_operations import check_logged_in

def main():
    check_logged_in()
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
    session.close()

    print(f"User {username} has been logged in.")

if __name__ == "__main__":
    main()