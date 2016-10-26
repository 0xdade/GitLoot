class User:

	def __init__(self, json):
		# Init user object.
		self.id = json['id']
		self.login = json['login']
		self.email = json['email']
		self.company = json['company']
		self.blog = json['blog']
		self.repoCount = json['public_repos']
		self.url = json['url']
		self.reposUrl = json['repos_url']
		self.created_at = json['created_at']
		self.updated_at = json['updated_at']
		self.repos = {}

	def __str__(self):
		repoList = ""
		for repo in self.repos:
			repoList += str(repo) + ","
		return "User: " + str(self.id) + ", " + str(self.login) + ", " + str(self.repoCount) + "\nRepos: " + repoList[:-1]

	def getRepos(self):
		return self.repos.items()