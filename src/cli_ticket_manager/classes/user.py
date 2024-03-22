from dataclasses import dataclass
from .session import Session

@dataclass
class User:
	"""
	Class for keeping track of user information and
	"connection" to ticket manager.
	"""
	username: str
	team: str
	session: Session = None

	def log_in(self):
		if self.is_logged_in():
			print("Already logged in.")
		
		self.session = Session()
		
	def log_out(self):
		if not self.is_logged_in():
			print("Already not logged in.")
		
		self.session.save_tickets()
		self.session = None

	def is_logged_in(self):
		return self.session != None