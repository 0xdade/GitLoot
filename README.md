# GitTreasure

This tool began as a red team project to simply automate gitrob against our enterprise Github installation so that we could broadly scan to find potentially valuable information. After a bit of work, I had built an automated tool that collects a list of all users and organizations and passes them along to gitrob for the actual analysis. But when I finished this, I noticed several issues I was having with gitrob during the analysis stage, and the web app simply crumbled under the weight of the number of repositories we were assessing. Gitrob hasn't seen an update in six months, and I don't really enjoy writing ruby, so I decided I'd start my own implementation.

Things I cared about in my new implementation:
- Extensibility. 
	- I want to be able to add new ways to store the data, and new ways to collect the data, with relative ease.
- Historical analysis. 
	- I want to be able to scan previous commit objects for potentially sensitive information leaks.
- Recurring analysis. 
	- I want to regularly (and automatically) followup on repositories that I've been targeting. 
	- An option to set the update interval
- Local analysis. 
	- I'd prefer to clone the repository locally for analysis to reduce the number of api requests I need to make.
	- An option to maintain local copies of repositories we add.
- Whole API analysis
	- An easy way to automatically analyze the entire contents of an API. This is primarily useful for enterprise github installations.

One thing that I thought about when I decided I was going to build my own version was about the ability to expand out onto other APIs and different storage mechanisms with relative ease. I also wanted to be able to scan the history of a repo to see if any sensitive information was stored in past commits that wasn't properly stripped. Even if they aren't valid credentials anymore, it may give us other interesting information.

I also wanted it to be able to regularly monitor our targets. Combining this with the ability to analyze the historical commits meant that we'd also need to keep track of the most recent commit we analyzed for a given repo. We're also going to clone the repo locally and do our analysis locally as opposed to doing it via a ton of api requests, so we need to be able to delete the repo when we're done analyzing it (with an option to save all the repos locally, if you have enough storage for it).

## Clues

A clue is how you define the types of information you want to look for. A clue is a json file indicates the following:
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

A crate is how we store our findings. It implements the following:
- addUser(self, user)
- addOrganization(self, org)
- addRepository(self, repo)
- addLoot(self, loot)


## Maps

A map is how we know how to communicate with the api. It implements the following:
- getUser(self, username)
- getOrganization(self, orgName)
- getRepository(self, repoName)


## Models

A model is an object that represents data to be stored in a crate. 
