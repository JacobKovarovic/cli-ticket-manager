import json
from .ticket import Ticket

class Session:
	"""
	Class for accessing tickets from json data.
	"""

	def __init__(self):
		self._load_tickets()

	def _load_tickets(self):
		"""
		Postcondition: Tickets are loaded into tickets instance variable
		"""
		ticketFile = open("data/tickets.json", 'r+')
		fileContents = ticketFile.readline()
		if fileContents != '':
			self.tickets = [Ticket(*tuple(ticket)) for ticket in json.loads(fileContents)]
		else:
			self.tickets = []
	
	def _store_tickets(self):
		"""
		Postconditions: Old state of ticket list is overwritten with new state of ticket list.
		"""
		ticketFile = open("data/tickets.json", 'w')
		ticketFile.write(json.dumps([ticket.toList() for ticket in self.tickets]))
		ticketFile.close()

	def save_tickets(self):
		print("Saving tickets.")
		self._store_tickets()