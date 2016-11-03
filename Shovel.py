# Shovel abstraction allows us to interact with shovels without caring about the type of repository.
import shovels

class Shovel:
	def __init__(self, shovelType):
		if shovelType == "git":
			self._shovel = shovels.GitShovel()

	def setRepo(self, repo):
		self._shovel.setRepo(repo)
	
	def cleanUp(self):
		self._shovel.cleanUp()

	def clone(self):
		#clone the repo locally so that we can interact with it
		self._shovel.clone()

	def getHeadCommit(self):
		return self._shovel.getHeadCommit()

	def printRepo(self):
		self._shovel.printRepo()
		return

	def nextCommit(self):
		#get the next commit for inspection
		return self._shovel.nextCommit()