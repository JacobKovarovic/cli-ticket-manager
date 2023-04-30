session = open("session.json", 'r')
if session != '':
    session.close()
    session = open("session.json", 'w')
    session.write('')
else:
    print("User is not signed in.")

session.close()