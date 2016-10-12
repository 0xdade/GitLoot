# Facade for varying maps. 
import maps
class Map:
	
	def __init__(self, mapType):
		if mapType.lower() == "bitbucket":
			self._map = maps.BitbucketMap()
		else if mapType.lower() == "github":
			self._map = crates.GithubMap()

	def getUser(self, user):
		self._map.getUser(user)
		return 0

	def getOrganization(self, org):
		self._map.getOrganization(org)
		return 0

	def getRepository(self, repo, sinceCommit=None):
		self._map.getRepository(repo)
		return 0