# Jobs encapsulate the necessary information for the prospector to 

class Job:
	def __init__(self):
		self.createTime = 0
		self.finishTime = 0
		self.apiLink = ""				# The link to the api root that we build our queries off of.
		self.apiKeys = []				# The (list of) API key(s) to use when processing the job
		self.subject = ""				# The subject of the job. Could be a user, org, repo, or API. 
		self.rescanInterval = 0			# an integer representing the number of hours to go between rescans.
		self.crateType = "" 			# this allows us to store different jobs with different methods. Useful for running a job if you only want data dumped to a file.
		self.jobType = "" 				# (User, Org, Repo, API)
		self.parent = 0 				# Keep track of my parent job. If no parent, we can mark the job finished.
