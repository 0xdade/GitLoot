from ConfigParser import ConfigParser
import argparse
import Map
#from models import *

PROG_NAME = "GitLoot"
PROG_VER = 0.1
PROG_DESC = "Automatically perform analysis on repositories to look for valuable information."
PROG_EPILOG = "You know how to do it now, go forth and loot and pillage."


def loadConfig():
	config = ConfigParser()
	config.read("config.ini")
	par=dict(config.items("api"))
	for p in par:
	    	par[p]=par[p].split("#",1)[0].strip() # To get rid of inline comments

	globals().update(par)  #Make them availible globally

def parseArgs():
	parser = argparse.ArgumentParser(prog=PROG_NAME, description=PROG_DESC, epilog=PROG_EPILOG)
	parser.add_argument("--version", action="version", version="%(prog)s v"+str(PROG_VER))
	parser.add_argument("--add-job", nargs='?', dest="job_subject", help="A job can be a user, an org, or a repo.")
	parser.add_argument("--rescan", nargs='?', dest="job_rescan", help="How frequently you want to rescan. Examples include 1h, 24h, 7d.")
	parser.add_argument("--api", nargs='?', dest="job_api", help="The root of the api you want to use for the input job. This overrides the default set in the config.")
	parser.add_argument("--keys", nargs='?', dest="job_keys", help="An (optionally) comma separated list of api keys. A single key is fine for small jobs.")
	parser.add_argument("--crate", nargs='?', dest="job_crate", help="Method of storage you want to use to store output from the job.")

	args = parser.parse_args()
	return args

def main():
	#loadConfig()
	# We load the config first, and then read command line options. Command line can override options from the config at runtime.
	#args = parseArgs()
	#if args.job_subject:
		#We need to add a job to the jobs crate so the prospector can find it.

	
	gh = Map.Map('github')
	user = gh.getUser('0xdade')
	org = gh.getOrganization('b0tchsec')
	repo = gh.getRepository('0xdade', 'GitLoot')
	print str(user) + "\n" + str(org) + "\n" + str(repo)
	#print "I guess we're done here. . ."
	


if __name__ == '__main__':
	main()
