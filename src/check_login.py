from sys import exit

def check_login():
    session = open("session.json", 'r')
    if session.readline() != '':
        session.close()
        exit("User is already signed in. Please sign out to sign in as other user.")
    session.close()