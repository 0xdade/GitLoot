from ConfigParser import ConfigParser
from optparse import OptionParser

def loadConfig():
	config = ConfigParser()
	config.read("config.ini")
	par=dict(config.items("api"))
	for p in par:
	    	par[p]=par[p].split("#",1)[0].strip() # To get rid of inline comments

	globals().update(par)  #Make them availible globally
	par=dict(config.items("targets"))
	for p in par:
    		par[p]=par[p].split("#",1)[0].strip() # To get rid of inline comments
	globals().update(par)  #Make them availible globally

def parseOptions():
	parser = OptionParser()
	parser.add_option("")
	(options,args) = parser.parse_args()
	return options
def main():
	print "Initializing . . ."
	loadConfig()
	# We load the config first, and then read command line options. Command line can override options from the config at runtime.
	options = parseOptions()
	print ". . .Initialized."
	#Honestly I'm only commiting this because I wanted to save the design. 
	#I haven't started to flesh out the actual work yet.

	print "I guess we're done here. . ."
	


if __name__ == '__main__':
	main()
