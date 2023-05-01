from sys import exit
import json

def check_logged_in():
    session = open("session.json", 'r')
    if session.readline() != '':
        session.close()
        exit("User is already signed in. Please sign out to sign in as other user.")
    session.close()

def check_logged_out():
    session = open("session.json", 'r')
    if session.readline() == '':
        session.close()
        exit("You are not signed in. Please sign in to perform this operation.")
    session.close()

def get_loggedin_user():
    check_logged_out()
    session = open("session.json", 'r')
    user = json.loads(session.readline())
    session.close()
    return user