# Github api calls for common tasks
import requests
import re
from requests_oauthlib import OAuth1
from models import Organization, Repository, User
class GithubMap:
	
	def __init__(self, config=None):
		if config:
			self.CONFIG_FILE = config
		self.next = ""
		self.API_ROOT = r"https://api.github.com/" # We'll load this from config later
		self.GET_USER = self.API_ROOT + "users/"
		self.GET_USERS = self.API_ROOT + "users"
		self.GET_ORG = self.API_ROOT + "orgs/"
		self.GET_REPO = self.API_ROOT + "repos/"
		self.TOKENS = []
		self.current_token = 1
		self.HEADERS = {'user-agent': '0xdade/GitLoot', 'Authorization': "token %s" % self.TOKENS[self.current_token]}
		return

	def loadSettings(self):
		# Load settings from config file
		# Options include API_ROOT, TOKENS, user-agent
		return

	def getUsers(self):
		if self.next != "":
			r = self.makeRequest(self.next)
		else:
			r = self.makeRequest(self.GET_USERS)
		self.next = r.links["next"]['url']
		return r.json()

	def switchTokens(self):
		# switch to a new token
		if self.current_token == len(self.TOKENS):
			self.current_token = 1
		elif self.current_token < len(self.TOKENS):
			self.current_token += 1
		self.HEADERS['Authorization'] = "token %s" % self.TOKENS[self.current_token-1]
		return

	def makeRequest(self, entity):
		r = requests.get(entity, headers=self.HEADERS)
		if (int(r.headers['X-RateLimit-Remaining']) < 4950):
			self.switchTokens()
		if (r.status_code == 200):
			return r
		else:
			raise SystemExit(str(r.status_code) + ": Seems we've lost the way, sir.")

	def getUser(self, uname):
		# API call to fetch user
		r = self.makeRequest(self.GET_USER + uname)
		user = User(r.json())
		user.repos = self.getUserRepos(user)
		return user

	def getUserRepos(self, user):
		# Pending multipage handling
		repos = {}
		r = self.makeRequest(user.reposUrl)
		for repo in r.json():
			repos[repo['id']] = repo['full_name']
		return repos

	def getOrgRepos(self, org):
		# Pending multipage handling
		repos = {}
		r = self.makeRequest(org.reposUrl)
		for repo in r.json():
			repos[repo['id']] = repo['full_name']
		return repos

	def getOrganization(self, orgName):
		# API call to fetch organization
		r = self.makeRequest(self.GET_ORG + orgName)
		org = Organization(r.json())
		org.members = self.getOrganizationMembers(orgName)
		org.repos = self.getOrgRepos(org)
		return org

	def getOrganizationMembers(self,orgName):
		# API call to fetch list of public members of organization
		# Pending multipage handling
		members = {}
		r = self.makeRequest(self.GET_ORG + orgName + "/public_members")
		for member in r.json():
			members[member['id']] = member['login']
		return members

	def getRepository(self, full_name):
		# API call to fetch repository
		r = self.makeRequest(self.GET_REPO + full_name)
		repo = Repository(r.json())
		return repo