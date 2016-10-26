# Check if prereqs are installed

# Select crate type (how are we storing data?)

# Init database if necessary, get db creds

# Create directory structure if file crate.

# Set persistent information in config
# including default api, crate type, database credentials if applicable, lists of api keys, update interval
import pip

class Setup:

	def __init__(self):
		# Do all the setup on setup instantiation
		self.setupDependencies()
		self.setupConfig()
		self.setupCrate("MySQL")
		return

	def setupCrate(self, crateType):
		# initialize the crate matching crateType
		return
	
	def setupConfig(self):
		# Ask the user for details about how they are going to run the tool
		# Save this to ~/.gitloot
		return

	def setupDependencies(self):
		# pip install the requirements.txt file
		pip.main(['install', '-r', 'requirements.txt'])
		return

def main():
	# setup.py can run standalone or run automatically at first run.
	setup = Setup()

if __name__ == '__main__':
	main()