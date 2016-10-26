# Connector for storing loot in MySQL databases.
from ConfigParser import ConfigParser
class SQLCrate:
	def __init__(self, config=None):
		if config:
			self.CONFIG_FILE = config
		else:
			self.CONFIG_FILE = None
		self.db_name = ""
		self.db_user = ""
		self.db_pass = ""
		self.db_host = ""
		self.loadSettings()
		
	def loadSettings(self):
		# fetch settings from config file
		config = ConfigParser()
		if self.CONFIG_FILE:
			config.read(self.CONFIG_FILE)
		else:
			if not config.read(os.path.expanduser('~') + "/.gitloot"):
				raise IOError, "cannot load ~/.gitloot"
		confDict = dict(config.items(self.__class__.__name__))
		if (confDict['db_name']):
			self.db_name = confDict['db_name']
		if (confDict['db_user']):
			self.db_user = confDict['db_user']
		if (confDict['db_pass']):
			self.db_pass = confDict['db_pass']
		if (confDict['db_host']):
			self.db_host = confDict['db_host']
		return 0

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

	def addJob(self,job):
		#add job to a jobs table.
		return

	def finishJob(self,job):
		# This job is finished, let's update the record and set a finish time, create a new job w/ start time = finishTime + rescanInterval
		return