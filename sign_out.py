from src.user_operations import check_logged_out

check_logged_out()
session = open("session.json", 'w')
session.write('')
session.close()

print("User has been logged out.")