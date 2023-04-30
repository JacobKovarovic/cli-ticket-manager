from sys import exit

def checkLogin():
    session = open("session.json", 'r')
    if session.readline() != '':
        exit("User is already signed in. Please sign out to sign in as other user.")