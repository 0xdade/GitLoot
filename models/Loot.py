class Loot:


	def __init__(self):
		# Init user object.
		self.sourceRepo = 0 			# remote ID number of repo
		self.sourceUrl = "" 			# remote url to repo
		self.sourceOwner = 0 			# remote ID of user
		self.sourceHash = "" 			# Store the hash of the commit object we found this in
		self.author = "" 				# Author of the commit object we found loot in
		self.discoveryDate = 0			# Timestamp that we discovered this loot
		self.lootType = "" 				# Caption of the clue that characterized this as loot
		self.lootContents = "" 			# string representation of the loot found. 