# Prospector handles processing the job queue. This will use a synchronized queue so we can process jobs in parallel

class Prospector:

	def __init__(self):
		self.jobQueue = Queue()

	def addJob(self, job):
		# Add a job object to the end of the queue
		self.jobQueue.put(job)

	def getJob(self):
		# Allow a worker to get the next available job.
		return self.jobQueue.get()

	def jobsDone(self):
		# indicate that a job is finished. We can remove it from the queue and mark it as finished in the crate.
		self.jobQueue.task_done()

	def loadJobs(self, crate):
		# Load jobs from a crate into the job queue
		return

	def postJobs(self, crate):
		# Save job queue to a crate, in the event of a shutdown or crash.
		return