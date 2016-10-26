# Check if prereqs are installed

# Select crate type (how are we storing data?)

# Init database if necessary, get db creds

# Create directory structure if file crate.

# Set persistent information in config
# including default api, crate type, database credentials if applicable, lists of api keys, update interval



class Setup:

	def __init__(self):
		# Do all the setup on setup instantiation
		self.setupDependencies()
		self.setupConfig()
		self.setupCrate()
		return
	def printHeader(self, text):
		print ("#"*10) + "\n" + text + "\n" + ("#"* 10)

	def setupCrate(self):
		# initialize the crate matching crateType
		self.printHeader("CRATE SETUP")
		return

	def setupConfig(self):
		# Ask the user for details about how they are going to run the tool
		# Save this to ~/.gitloot
		self.printHeader("CONFIG FILE")
		print "What type of API is this? (github)"
		api_type = raw_input("API Type: ")
		print "Please let us know the root of the API that we'll be running against."
		api_root = raw_input("API Root: ")
		if api_root[-1] != "/":
			api_root = api_root + "/"
		print "Please enter API tokens as a comma separated list"
		api_tokens = raw_input("API Token(s): ")
		api_tokens = api_tokens.strip(" ")
		print "What user agent would you like to use?"
		user_agent = raw_input("User-Agent: ")
		import os
		configFile = os.path.expanduser('~') + "/.gitloot"

		if api_type.lower() == "github":
			confHeader = "[GithubMap]\n"
		else:
			print "We only support github APIs right now."
			confHeader = "[GithubMap]\n"
		with open(configFile, 'w+') as conf:
			conf.write(confHeader + "api_root=\"" + api_root + "\"\napi_tokens=\"" + api_tokens + "\"\nuser-agent=\"" + user_agent + "\"\n")
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