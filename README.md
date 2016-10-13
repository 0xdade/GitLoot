# GitLoot

This tool began as a red team project to simply automate gitrob against our enterprise Github installation so that we could broadly scan to find potentially valuable information. After a bit of work, I had built an automated tool that collects a list of all users and organizations and passes them along to gitrob for the actual analysis. But when I finished this, I noticed several issues I was having with gitrob during the analysis stage, and the web app simply crumbled under the weight of the number of repositories we were assessing. Gitrob hasn't seen an update in six months, and I don't really enjoy writing ruby, so I decided I'd start my own implementation.

## Design goals:
- Extensibility. 
	- I want to be able to add new ways to store the data, and new ways to collect the data, with relative ease.
- Historical analysis. 
	- I want to be able to scan previous commit objects for potentially sensitive information leaks.
	- An option to "Quickscan" and only look at the repo HEAD, for faster scans.
- Recurring analysis. 
	- I want to regularly (and automatically) followup on repositories that I've been targeting. 
	- An option to set the update interval
- Local analysis. 
	- I'd prefer to clone the repository locally for analysis to reduce the number of api requests I need to make.
	- An option to maintain local copies of repositories we add.
- Whole API analysis
	- An easy way to automatically analyze the entire contents of an API. This is primarily useful for enterprise github installations.


## Clues

A clue is how you define the types of information you want to look for. Clues get used by the metal detector to scan commits. A clue is a json file indicates the following:
- Part of the file to look at
	- Extension
	- Filename
	- Content
- Type of matching to do
	- Match
	- regex
- Pattern
	- Exact match on filename or extension
	- Regex match on extension, filename, or content
- Caption
	- Short description of what this clue looks for
- Description
	- Why you are looking for this clue
	
I'm using this design so that you can import existing signatures from [gitrob](https://github.com/michenriksen/gitrob/blob/master/signatures.json)


## Crates

A crate is how we store our findings. It needs to be able to accept users, organizations, repositories, and loot. It implements the following:
- addUser(self, user)
- addOrganization(self, org)
- addRepository(self, repo)
- addLoot(self, loot)


## Loot

Loot represents potentially valuable information, as defined by our clues. Loot is created by the metal detector and then passed to a crate.

## Maps

A map is how we know how to communicate with the api. It needs to be able to fetch information about a user, an organization, and a repository based on a given string. A map also handles cycling out API keys when rate limits are hit. It implements the following:
- getUser(self, username)
- getOrganization(self, orgName)
- getRepository(self, repoName)


## Metal Detector

The metal detector inspects commit objects, looking for clues. If it finds clues, it creates loot and puts it in a crate.


## Models

Models represent entities which we act upon to store and move data around the application.


## Prospector

The prospector handles the job queue, dispatching jobs for processing as they are ready. 


## Shovels

A shovel is how we interact with a repository, iterating through commits and passing them to the metal detector. It takes a repository model at initialization and clones the repo locally. It creates commit objects to be passed to the metal detector. My initial plan is only to support git, however I'm designing it to (more) easily expand to other repo types if desirable.
