from ConfigParser import ConfigParser
import argparse
import Map
import Shovel
import MetalDetector
from setup import Setup
import os
import git
#from models import *

PROG_NAME = "GitLoot"
PROG_VER = 0.1
PROG_DESC = "Automatically perform analysis on repositories to look for valuable information."
PROG_EPILOG = "You know how to do it now, go forth and loot and pillage."
DEPTH = 1

def parseArgs():
	parser = argparse.ArgumentParser(prog=PROG_NAME, description=PROG_DESC, epilog=PROG_EPILOG)
	parser.add_argument("--version", action="version", version="%(prog)s v"+str(PROG_VER))
#	parser.add_argument("--api", nargs='?', dest="job_api", help="The root of the api you want to use for the input job. This overrides the default set in the config.")
#	parser.add_argument("--keys", nargs='?', dest="job_keys", help="An (optionally) comma separated list of api keys. A single key is fine for small jobs.")
	parser.add_argument("--depth", dest="depth", default=1, help="Scan depth [Default 1]")
	parser.add_argument("-o", "--org", dest="org", help="Scan an organization's repositories")
	parser.add_argument("-r", "--repository", dest="repo", help="Scan a single repository. Use the full name. E.g. '0xdade/GitLoot'")
	parser.add_argument("-u", "--user", dest="user", help="Scan a user's repositories.")
	parser.add_argument("-m", "--members", action="store_true", default=False, dest="members", help="Search the repositories of every member of an organization.")
	args = parser.parse_args()
	if not args.org and not args.repo and not args.user:
		print "You must supply either -o, -r, or -u."
		raise SystemExit(-1)
	if args.org and (args.repo or args.user):
		print "Please supply only one target with -o, -r, or -u."
		raise SystemExit(-1)
	if args.repo and (args.org or args.user):
		print "Please supply only one target with -o, -r, or -u."
		raise SystemExit(-1)
	if args.user and (args.org or args.repo):
		print "Please supply only one target with -o, -r, or -u."
		raise SystemExit(-1)
	if args.repo and '/' not in args.repo:
		print "Please supply the full name of the repo. E.g. '0xdade/GitLoot'"
		raise SystemExit(-1)
	DEPTH = args.depth
	return args

def scanRepo(mmap,shovel,detector,target):
	repo = mmap.getRepository(target)
	shovel.setRepo(repo)
	shovel.clone()
	commitCount = 0
	for commit in shovel.nextCommit():
		if commitCount < DEPTH:
			cluesFound = detector.processCommit(commit)
			commitCount+=1
		else:
			print "Clues Found: " + str(cluesFound)
			break
	shovel.cleanUp()

def scanUser(mmap,shovel,detector,target):
	repos = target.getRepos()
	for rid,full_name in repos:
		scanRepo(mmap,shovel,detector,full_name)

def scanOrg(mmap,shovel,detector,target,members):
	org = gh.getOrganization(target)
	repos = target.getRepos()
	for rid,full_name in repos:
		scanRepo(mmap,shovel,detector,full_name)
	if members:
		for uid,login in org.getMembers():
			user = gh.getUser(login)
			scanUser(mmap,shovel,detector,user)


def main():
	if not (os.path.isfile(os.path.expanduser('~') + "/.gitloot")):
		# config not found, we need to prompt the user for config settings
		setup = Setup()
		print "Setup completed successfully. Please re-run GitLoot to begin."
		raise SystemExit(0)
	# We load the config first, and then read command line options. Command line can override options from the config at runtime.
	args = parseArgs()

	gh = Map.Map('github')
	shovel = Shovel.Shovel('git')
	md = MetalDetector.MetalDetector()

	if args.org:
		scanOrg(gh, shovel, md, args.org, args.members)
	elif args.user:
		scanUser(gh, shovel, md, args.user)
	elif args.repo:
		scanRepo(gh, shovel, md, args.repo)

	#myRepo = gh.getRepository('0xdade/GitLoot')
	#print str(org) + "\n"
	# for rid,full_name in org.getRepos():
	# 	repo = gh.getRepository(full_name)
	# 	shovel.setRepo(repo)
	# 	shovel.clone()
	# 	shovel.cleanUp()
	# 	print str(repo) + "\n"		
	
	# for uid,login in org.getMembers():
	# 	user = gh.getUser(login)
	# #	print str(user) + "\n"
	# 	for rid,full_name in user.getRepos():
	# 		repo = gh.getRepository(full_name)
	# 		shovel.setRepo(repo)
	# 		shovel.clone()
	# 		print "\n" + str(repo)
	# 		commitCount = 0
	# 		for commit in shovel.nextCommit():
	# 			if commitCount < args.depth:
	# 				cluesFound = md.processCommit(commit)
	# 				commitCount+=1
	# 			else:
	# 				print "Clues Found: " + str(cluesFound)
	# 				break

	# 		shovel.cleanUp()
	# #gh.getUsers()
	# #print "I guess we're done here. . ."


if __name__ == '__main__':
	main()
