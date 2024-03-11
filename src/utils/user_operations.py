"""
Collection of functions used in frontend scripts.
"""

from sys import exit
import json
from utils.tickets import Ticket

def check_logged_in():
    """
    Raises error if a user is signed in.
    """
    session = open("session.json", 'r')
    if session.readline() != '':
        session.close()
        exit("User is already signed in. Please sign out to sign in as other user.")
    session.close()

def check_logged_out():
    """
    Raises error if a user is not signed in.
    """
    session = open("session.json", 'r')
    if session.readline() == '':
        session.close()
        exit("You are not signed in. Please sign in to perform this operation.")
    session.close()

def get_loggedin_user():
    """
    Return: Logged in user information in form [username, team]
    """
    check_logged_out()
    session = open("session.json", 'r')
    user = json.loads(session.readline())
    session.close()
    return user

def load_tickets():
    """
    Return: List of all existing tickets.
    """
    ticketFile = open("tickets.json", 'r+')
    fileContents = ticketFile.readline()
    if fileContents != '':
        allTickets = [Ticket(*tuple(ticket)) for ticket in json.loads(fileContents)]
    else:
        allTickets = []
    return allTickets

def store_tickets(tickets):
    """
    Postconditions: Old state of ticket list is overwritten with new state of ticket list.
    """
    ticketFile = open("tickets.json", 'w')
    ticketFile.write(json.dumps([ticket.toList() for ticket in tickets]))
    ticketFile.close()

if __name__ == "__main__":
    pass