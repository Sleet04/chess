class LogUtil :

	def __init__(self):
		pass

	def logPrinter(logTrack) :
		with open('log.txt','w') as logFile :
			logFile.write(repr(logTrack))