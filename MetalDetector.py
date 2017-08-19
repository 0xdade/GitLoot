# Pass in commit objects, study the blobs, attempt to match on clues specified in ./clues/*.json
# When clue is found, create new Loot and pass to crate
import glob, git, json
class MetalDetector:
	def __init__(self):
		self.contents = json.load(open('clues/contents.json'))
		self.extensions = json.load(open('clues/extensions.json'))
		self.filenames = json.load(open('clues/filenames.json'))
		self.messages = json.load(open('clues/messages.json'))
		self.paths = json.load(open('clues/paths.json'))
		print "MetalDetector: loaded %s clues" % (len(self.contents) + len(self.extensions) + len(self.filenames) + len(self.messages) + len(self.paths))

	def scanContents(self, content):
		for clue in self.contents:
			if clue['type'] == "match" and clue['pattern'] == content:
				print "FOUND A CLUE: " + content
		#print "Content: " + content
		pass

	def scanExtension(self, extension):
		for clue in self.extensions:
			if clue['type'] == "match" and clue['pattern'] == extension:
				print "FOUND A CLUE: " + extension
		#print "Extension: " + extension
		pass

	def scanFilename(self, filename):
		for clue in self.filenames:
			if clue['type'] == "match" and clue['pattern'] == filename:
				print "FOUND A CLUE: " + filename
		#print "Filename: " + filename
		pass

	def scanMessage(self, message):
		for clue in self.messages:
			if clue['pattern'] in message:
				print "FOUND A CLUE: " + message

	def scanPath(self, path):
		for clue in self.paths:
			if clue['type'] == "match" and clue['pattern'] == path:
				print "FOUND A CLUE: " + path
		#print "Path: " + path
		pass

	def processTree(self, tree, count):
		count = count
		for item in tree:
			if type(item) is git.objects.tree.Tree:
				#print "-"*count + "T: " + str(item)
				self.processTree(item, count+1)
			if type(item) is git.objects.blob.Blob:
				#print "-"*count + "B: " + str(item)
				self.scanPath(item.path)
				self.scanFilename(item.name)
				if len(item.name.rsplit('.', 1)) > 1:
					self.scanExtension(item.name.rsplit('.', 1)[1])
				self.scanContents(item.data_stream.read())

	def processCommit(self, commit):
		print "#"*10 + "\nC: " + str(commit) + "\n" + "#"*10
		self.scanMessage(commit.message)
		self.processTree(commit.tree,1)