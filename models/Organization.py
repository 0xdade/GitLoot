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

	def __str__(self):
		memberList = ""
		for member in self.members:
			memberList += str(member) + ","
		return "Organization: " + str(self.id) + ", " + str(self.login) + "\n\tMembers: " + memberList[:-1]