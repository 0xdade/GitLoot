from collections import deque
class Repository:

	def __init__(self, json):
		self.id = json['id']
		self.owner = json['owner']['id']
		self.name = json['name']
		self.full_name = json['full_name']
		self.url = json['url']
		self.cloneUrl = json['clone_url']
		self.commits = deque()

	def __str__(self):
		return "Repository: " + str(self.id) + ", " + str(self.full_name)