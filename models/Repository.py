from collections import deque
class Repository:

	def __init__(self):
		# Init user object.
		self.id = 0
		self.owner = 0
		self.name = ""
		self.url = ""
		self.cloneUrl = ""
		self.commits = deque()