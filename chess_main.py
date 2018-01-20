import sys , pygame
from pygame.locals import *
import csv
import math 
import utils
import logUtil

def __initiateGame__() :
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	menuWidth = 160
	TOTALWIDTH = 1600
	TOTALHEIGHT = 900
	cellWidth = 175
	cellInfoWidth = 40
	cellLineWidth = 4
	cellHeight = int(math.ceil(float((TOTALHEIGHT-cellInfoWidth))/8))

	#initiate the UI
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((TOTALWIDTH,TOTALHEIGHT))
	DISPLAYSURF.fill(WHITE)
	pygame.display.set_caption("chess")

	#initiate Utils
	logger = logUtil.LogUtil()
	utilsObj = utils.Utils(DISPLAYSURF)


	# initiate the chess board
	utilsObj.setBoard (DISPLAYSURF,menuWidth,TOTALWIDTH,TOTALHEIGHT,cellWidth,cellInfoWidth,cellLineWidth,cellHeight)
	utilsObj.dwnImg()

	while True : 
		for event in pygame.event.get() :
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()




if __name__ == '__main__':
	__initiateGame__()
	