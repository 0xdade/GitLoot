class Map:
	
	def __init__(self, mapType):
		import maps
		if mapType.lower() == "bitbucket":
			self._map = maps.BitbucketMap()
		elif mapType.lower() == "github":
			self._map = maps.GithubMap()

	def getUser(self, user):
		return self._map.getUser(user)

	def getOrganization(self, orgName):
		return self._map.getOrganization(orgName)

	def getOrganizationMembers(self,orgName):
		return self._map.getOrganizationMembers(orgName)

	def getRepository(self, owner, repo):
		return self._map.getRepository(owner, repo)