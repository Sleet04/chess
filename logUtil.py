class LogUtil :

	def __init__(self):
		pass

	def logPrinter(self,logTrack) :
		with open('log.txt','a') as logFile :
			logFile.write('\n'+repr(logTrack))