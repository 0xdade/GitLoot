# Pass in commit objects, study the blobs, attempt to match on clues specified in ./clues/*.json
# When clue is found, create new Loot and pass to crate
import glob, git, json, re
class MetalDetector:
	def __init__(self):
		self.contents = json.load(open('clues/contents.json'))
		self.extensions = json.load(open('clues/extensions.json'))
		self.filenames = json.load(open('clues/filenames.json'))
		self.messages = json.load(open('clues/messages.json'))
		self.paths = json.load(open('clues/paths.json'))
		print "MetalDetector: loaded %s clues" % (len(self.contents) + len(self.extensions) + len(self.filenames) + len(self.messages) + len(self.paths))

	def scanContents(self, content):
		clueCounter = 0
		for clue in self.contents:
			try:
				if clue['type'] == "match":
					for line in content.split('\n'):
						if clue['pattern'] in line:
							print "CONTENT MATCH CLUE: " + line
							clueCounter += 1
				if clue['type'] == "regex":
					match = re.search(clue['pattern'], content)
					if match != None:
						print "CONTENT REGEX CLUE: " + str(match.groups())
						clueCounter += 1
			except UnicodeDecodeError:
				pass
		return clueCounter

	def scanExtension(self, extension):
		clueCounter = 0
		for clue in self.extensions:
			try:
				if clue['type'] == "match" and clue['pattern'] == extension:
					print "EXTENSION MATCH CLUE: " + extension
					clueCounter += 1
				if clue['type'] == "regex" and (re.search(clue['pattern'], extension) != None):
					print "EXTENSION MATCH CLUE: " + extension
					clueCounter += 1
			except UnicodeDecodeError:
				pass
		return clueCounter

	def scanFilename(self, filename):
		clueCounter = 0
		for clue in self.filenames:
			try:
				if clue['type'] == "match" and clue['pattern'] == filename:
					print "FILENAME MATCH CLUE: " + filename
					clueCounter += 1
				if clue['type'] == "regex" and (re.search(clue['pattern'], filename) != None):
					print "FILENAME REGEX CLUE: " + filename
					clueCounter += 1
			except UnicodeDecodeError:
				pass
		return clueCounter

	def scanMessage(self, message):
		clueCounter = 0
		for clue in self.messages:
			try:
				if clue['pattern'] in message:
					print "MESSAGE MATCH CLUE: " + message
					clueCounter += 1
			except UnicodeDecodeError:
				pass
		return clueCounter

	def scanPath(self, path):
		clueCounter = 0
		for clue in self.paths:
			try:
				if clue['type'] == "match" and clue['pattern'] == path:
					print "PATH MATCH CLUE: " + path
					clueCounter += 1
				if clue['type'] == "regex" and (re.search(clue['pattern'], path) != None):
					print "PATH REGEX CLUE: " + path
					clueCounter += 1
			except UnicodeDecodeError:
				pass
		return clueCounter

	def processTree(self, tree, count):
		count = count
		clueCount = 0
		for item in tree:
			if type(item) is git.objects.tree.Tree:
				clueCount += self.processTree(item, count+1)
			if type(item) is git.objects.blob.Blob:
				#print "-"*count + "B: " + str(item)
				clueCount += self.scanPath(item.path)
				clueCount += self.scanFilename(item.name)
				if len(item.name.rsplit('.', 1)) > 1:
					clueCount += self.scanExtension(item.name.rsplit('.', 1)[1])
				clueCount += self.scanContents(item.data_stream.read())
		return clueCount

	def processCommit(self, commit):
		#print "#"*10 + "\nC: " + str(commit) + "\n" + "#"*10
		clueCount = 0
		clueCount += self.scanMessage(commit.message)
		#print commit.author.email
		clueCount += self.processTree(commit.tree,1)
		return clueCount