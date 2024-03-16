"""
Precondition: User must be logged in
Postcondition: User is logged out, data in session file is deleted
"""

from utils.user_operations import check_logged_out

def main():
    check_logged_out()
    session = open("session.json", 'w')
    session.write('')
    session.close()

    print("User has been logged out.")

if __name__ == "__main__":
    main()