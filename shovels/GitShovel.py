# Git Shovel handles interacting with git repositories. Probably going to use GitPython
# The shovel combs through a repository and creates commit objects to be analyzed
import git
import shutil
class GitShovel:
	def __init__(self):
		self.path = "workbench/"
		self.repo = ""
		self.cloned_repo = None
		return

	def setRepo(self, repo):
		self.repo = repo
		self.path = "workbench/" + repo.full_name

	def clone(self):
		#clone the repo locally so that we can interact with it
		self.cloned_repo = git.Repo.clone_from(self.repo.cloneUrl, self.path)
		return

	def cleanUp(self):
		self.repo = None
		shutil.rmtree(self.path)
		self.path =  "workbench/"
		self.cloned_repo = None



	def nextCommit(self):
		#get the next commit for inspection
		return