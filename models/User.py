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

	def __str__(self):
		return "User: " + str(self.id) + ", " + str(self.login) + ", " + str(self.repoCount)