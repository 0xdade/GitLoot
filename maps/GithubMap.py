# Github api calls for common tasks
import requests
from requests_oauthlib import OAuth1
from models import Organization, Repository, User
class GithubMap:
	
	def __init__(self):
		self.API_ROOT = r"https://api.github.com/" # We'll load this from config later
		self.GET_USER = self.API_ROOT + "users/"
		self.GET_ORG = self.API_ROOT + "orgs/"
		self.GET_REPO = self.API_ROOT + "repos/"
		self.TOKENS = ["494e7e43eb9ced4b2116b4cc68f0621ea531c802", "d3cebe1bb0960a3d8baf1ed73e278045e1d9fee4"]
		self.CURRENT_TOKEN = 1
		self.HEADERS = {'user-agent': '0xdade/GitLoot', 'Authorization': "token %s" % self.TOKENS[self.CURRENT_TOKEN]}
		return

	def switchTokens(self):
		# switch to a new token
		if self.CURRENT_TOKEN == len(self.TOKENS):
			self.CURRENT_TOKEN = 1
		elif self.CURRENT_TOKEN < len(self.TOKENS):
			self.CURRENT_TOKEN += 1
		return

	def makeRequest(self, entity):
		r = requests.get(entity, headers=self.HEADERS)
		if (r.headers['X-RateLimit-Remaining'] < 10):
			self.switchTokens()
		if (r.status_code == 403):
			raise SystemExit("Seems we've lost the keys, sir.")
		return r

	def getUser(self, user):
		# API call to fetch user
		r = self.makeRequest(self.GET_USER + user)
		if (r.status_code == 200):
			user = User(r.json())
			return user
		else:
			return r.status_code

	def getOrganization(self, orgName):
		# API call to fetch organization
		r = self.makeRequest(self.GET_ORG + orgName)
		if (r.status_code == 200):
			org = Organization(r.json())
			org.members = self.getOrganizationMembers(orgName)
			return org
		else:
			return r.status_code

	def getOrganizationMembers(self,orgName):
		# API call to fetch list of public members of organization
		members = {}
		r = self.makeRequest(self.GET_ORG + orgName + "/public_members")
		if (r.status_code == 200):
			for member in r.json():
				members[member['id']] = self.getUser(member['login'])
		return members

	def getRepository(self, owner, repo):
		# API call to fetch repository
		r = self.makeRequest(self.GET_REPO + owner + "/" + repo)
		if (r.status_code == 200):
			repo = Repository(r.json())
			return repo
		else:
			return r.status_code