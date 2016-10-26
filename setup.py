# Check if prereqs are installed
# Set persistent information in config
from ConfigParser import ConfigParser
import os
class Setup:

	def __init__(self):
		# Do all the setup on setup instantiation
		self.setupDependencies()
		self.setupMap()
		self.setupCrate()
		return

	def printHeader(self, text):
		print ("#"*10) + "\n" + text + "\n" + ("#"* 10)

	def setupCrate(self):
		# initialize the crate matching crateType
		config = ConfigParser()
		config.read(os.path.expanduser('~') + "/.gitloot")
		try:
			crateDict = dict(config.items("SQLCrate"))
			return
		except:
			self.printHeader("CRATE SETUP")
			crate_type = "sql"
			db_name = raw_input("Database name: ")
			db_user = raw_input("Database user: ")
			db_pass = raw_input("Database pass: ")
			db_host = raw_input("Database host: ")

			configFile = os.path.expanduser('~') + "/.gitloot"
			if crate_type.lower() == "sql":
				confHeader = "\n[SQLCrate]\n"
			else:
				print "We only support SQL crates right now."
				confHeader = "\n[SQLCrate]\n"
			with open(configFile, 'a') as conf:
				conf.write(confHeader + "db_name=%s\ndb_user=%s\ndb_pass=%s\ndb_host=%s\n" % (db_name, db_user, db_pass, db_host))
			return


		
	def setupMap(self):
		# Ask the user for details about how they are going to run the tool
		# Save this to ~/.gitloot
		config = ConfigParser()
		config.read(os.path.expanduser('~') + "/.gitloot")
		try:
			mapDict = dict(config.items("GithubMap"))
			return
		except:
			self.printHeader("MAP SETUP")
			#print "What type of API is this? (github)"
			#api_type = raw_input("API Type: ")
			api_type = "github" # Commented out the question about this, it's unnecessary at the moment.
			print "Please provide the API root URI that we'll be running against. (https://api.github.com)"
			api_root = raw_input("API Root: ")
			if api_root[-1] != "/":
				api_root = api_root + "/"
			print "Please enter API tokens as a comma separated list"
			api_tokens = raw_input("API Token(s): ")
			api_tokens = api_tokens.strip(" ")
			print "What user agent would you like to use?"
			user_agent = raw_input("User-Agent: ")
			configFile = os.path.expanduser('~') + "/.gitloot"

			if api_type.lower() == "github":
				confHeader = "[GithubMap]\n"
			else:
				print "We only support github APIs right now."
				confHeader = "\n[GithubMap]\n"
			with open(configFile, 'a') as conf:
				conf.write(confHeader + "api_root=\"%s\"\napi_tokens=\"%s\"\nuser-agent=\"%s\"\n" % (api_root, api_tokens, user_agent))
			return

	def setupDependencies(self):
		# pip install the requirements.txt file
		try:
			import pip
			self.printHeader("DEPENDENCIES")
			pip.main(['install', '-r', 'requirements.txt'])
		except ImportError:
			print "Please install pip to continue. . ."
			raise SystemExit(1)
		return

def main():
	# setup.py can run standalone or run automatically at first run.
	setup = Setup()

if __name__ == '__main__':
	main()