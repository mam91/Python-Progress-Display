class progress(object):
	def __init__(self, total):
		self.percent = -1
		self.backspaceLen = 0
		self.total = total
 
	def updatePercent(self, current):
		newPercent = int(current / self.total * 100)
		if newPercent > self.percent:
			self.backspaceLen = 0 if self.percent < 0 else len(str(self.percent)) + 1
			self.percent = newPercent
			self.printPercent()

	def printPercent(self):
		backspaceStr = ""
		for _ in range(self.backspaceLen): backspaceStr += "\b"
		print(backspaceStr + str(self.percent) + "%", end="", flush=True)

	def close(self):
		print("", end="\n", flush=True)