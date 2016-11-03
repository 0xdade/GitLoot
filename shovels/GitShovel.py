# Git Shovel handles interacting with git repositories. Probably going to use GitPython
# The shovel combs through a repository and creates commit objects to be analyzed
import git
import shutil
class GitShovel:
	def __init__(self):
		self.path = "workbench/"
		self.repo = ""
		self.cloned_repo = None
		self.commits = None
		return

	def setRepo(self, repo):
		self.repo = repo
		self.path = "workbench/" + repo.full_name

	def clone(self):
		#clone the repo locally so that we can interact with it
		self.cloned_repo = git.Repo.clone_from(self.repo.cloneUrl, self.path)#, depth=1)
		self.commits = self.cloned_repo.iter_commits()
		return

	def cleanUp(self):
		self.repo = None
		shutil.rmtree(self.path)
		self.path =  "workbench/"
		self.cloned_repo = None

	def getHeadCommit(self):
		return self.cloned_repo.head.commit

	def printRepo(self):
		for commit in self.commits:
			print commit

	def nextCommit(self):
		#get the next commit for inspection
		for commit in self.commits:
			yield commit
		raise StopIteration