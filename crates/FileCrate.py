# Used to store loot in files.

class FileCrate:
	def __init__(self):
		self.rootDir = "."
		

	def addUser(self, user):
		#add a user file to our directory. domain/user
		return

	def addOrganization(self, org):
		#add an org file to our directory. domain/org
		#keep a list of users inside our org file.
		return

	def addRepository(self, repo):
		#add a repo to our directory domain/(user|org)/reponame
		return

	def addLoot(self, loot):
		#add loot to the loot directory. Store under domain/loot/reponame/timestamp-loottype.json
		return

	def addJob(self,job):
		#add job to a jobs directory. /domain/jobs/jobnum
		return

	def finishJob(self,job):
		# This job is finished, let's update the record and set a finish time, create a new job w/ start time = finishTime + rescanInterval
		return