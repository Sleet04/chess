class Data :

	TOTALWIDTH = None
	TOTALHEIGHT = None
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	menuWidth = TOTALWIDTH/10
	cellWidth = (TOTALWIDTH-menuWidth-cellInfoWidth)/8
	cellInfoWidth = 40
	cellLineWidth = 4
	cellHeight = int(math.ceil(float((TOTALHEIGHT-cellInfoWidth))/8))


	def __init__(self,TOTALWIDTH,TOTALHEIGHT) :
		self.TOTALWIDTH = TOTALWIDTH
		self.TOTALHEIGHT = TOTALHEIGHT