# Connector for storing loot in MySQL databases.

class MySQLCrate:
	def __init__(self):
		self.db_name = ""
		self.db_user = ""
		self.db_pass = ""
		self.db_host = ""
		
	def addUser(self, user):
		#add a user to the user table
		return 0

	def addOrganization(self, org):
		#add an org to the org table
		#add org<->member to a table that tracks members of an org
		return 0

	def addRepository(self, repo):
		#add a repo to repo table
		#foreign key on repoOwner to an org or user id
		return 0

	def addLoot(self, loot):
		#add loot to the loot table
		return 0