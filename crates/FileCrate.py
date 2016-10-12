# Used to store loot in files.

class FileCrate:
	def __init__(self):
		self.rootDir = "."
		

	def addUser(self, user):
		#add a user file to our directory. domain/user
		return 0

	def addOrganization(self, org):
		#add an org file to our directory. domain/org
		#keep a list of users inside our org file.
		return 0

	def addRepository(self, repo):
		#add a repo to our directory domain/(user|org)/reponame
		return 0

	def addLoot(self, loot):
		#add loot to the loot directory. Store under domain/loot/reponame/timestamp-loottype.json
		return 0