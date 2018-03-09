class progress(object):
	def __init__(self, total):
		self.percent = -1
		self.total = total
 
	def updatePercent(self, current):
		newPercent = int(current / self.total * 100)
		if newPercent > self.percent:
			self.percent = newPercent
			self.printPercent()
			
	def printPercent(self):
		print(str(self.percent) + "%\r", end="", flush=True)