# Shovel abstraction allows us to interact with shovels without caring about the type of repository.
import shovels

class Shovel:
	def __init__(self, repo, shovelType):
		self.repo = repo
		if shovelType == "git":
			self._shovel = shovels.GitShovel()

	def clone(self):
		#clone the repo locally so that we can interact with it
		self._shovel.clone()

	def nextCommit(self):
		#get the next commit for inspection
		return self._shovel.nextCommit()