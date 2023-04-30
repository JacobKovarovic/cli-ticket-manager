from sys import exit
import json

def check_login():
    session = open("session.json", 'r')
    if session.readline() != '':
        session.close()
        exit("User is already signed in. Please sign out to sign in as other user.")
    session.close()

def get_loggedin_user():
    check_login()
    session = open("session.json", 'r')
    user = json.loads(session.readline())
    session.close()
    return user