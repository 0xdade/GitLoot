class Organization:

	def __init__(self,json):
		# Init user object.
		self.id = json['id']
		self.login = json['login']
		self.email = json['email']
		self.blog = json['blog']
		self.repoCount = json['public_repos']
		self.url = json['url']
		self.reposUrl = json['repos_url']
		self.members = {}
		self.repos = {}

	def __str__(self):
		memberList = ""
		repoList = ""
		for member in self.members:
			memberList += str(member) + ","
		for repo in self.repos:
			repoList += str(repo) + ","
		return "Organization: " + str(self.id) + ", " + str(self.login) + "\nMembers: " + memberList[:-1] + "\nRepos: " + repoList[:-1]