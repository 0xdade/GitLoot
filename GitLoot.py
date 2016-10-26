from ConfigParser import ConfigParser
import argparse
import Map
from setup import Setup
import os
#from models import *

PROG_NAME = "GitLoot"
PROG_VER = 0.1
PROG_DESC = "Automatically perform analysis on repositories to look for valuable information."
PROG_EPILOG = "You know how to do it now, go forth and loot and pillage."

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
	if not (os.path.isfile(os.path.expanduser('~') + "/.gitloot")):
		# config not found, we need to prompt the user for config settings
		setup = Setup()
		print "Setup completed successfully. Please re-run GitLoot to begin."
		raise SystemExit(0)
	# We load the config first, and then read command line options. Command line can override options from the config at runtime.
	#args = parseArgs()
	#if args.job_subject:
		#We need to add a job to the jobs crate so the prospector can find it.

	
	gh = Map.Map('github')
	org = gh.getOrganization('b0tchsec')
	print str(org) + "\n"
	for rid,full_name in org.getRepos():
		repo = gh.getRepository(full_name)
		print str(repo) + "\n"		
	
	for uid,login in org.getMembers():
		user = gh.getUser(login)
		print str(user) + "\n"
		for rid,full_name in user.getRepos():
			repo = gh.getRepository(full_name)
			print str(repo) + "\n"
	#gh.getUsers()
	#print "I guess we're done here. . ."
	


if __name__ == '__main__':
	main()
