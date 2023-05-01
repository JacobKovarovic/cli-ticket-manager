from src.user_operations import check_logged_out, load_tickets

check_logged_out()
allTickets = load_tickets()
if allTickets == []:
    print("No tickets to list.")
else:
    for ticket in allTickets:
        print(ticket)