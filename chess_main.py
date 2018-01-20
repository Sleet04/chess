import sys , pygame
from pygame.locals import *
import csv
import math 
import utils

pygame.init()

def logUtils(logTrack) :
	with open('log.txt','w') as logFile :
		logFile.write(repr(logTrack))

BLACK = (0,0,0)
WHITE = (255,255,255)
menuWidth = 160
TOTALWIDTH = 1600
TOTALHEIGHT = 900
cellWidth = 175
cellInfoWidth = 40
cellLineWidth = 4
cellHeight = int(math.ceil(float((TOTALHEIGHT-cellInfoWidth))/8))



DISPLAYSURF = pygame.display.set_mode((TOTALWIDTH,TOTALHEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("chess")

utilsObj = utils.Utils(DISPLAYSURF)


# initiate the chess board
utilsObj.setBoard (DISPLAYSURF,menuWidth,TOTALWIDTH,TOTALHEIGHT,cellWidth,cellInfoWidth,cellLineWidth,cellHeight)
utilsObj.dwnImg()


	# to log the board
	# with open('log.txt','w') as logFile :
	# 	writer = csv.writer(logFile)
	# 	[writer.writerow(r) for r in board]




#  #lignes horizontales
# for i in range(200,1800,195) :

# 	pygame.draw.line(DISPLAYSURF,BLACK,(i,0),(i,960),4)

#  #lignes verticales
# for i in range(120,1000,120) :
# 	pygame.draw.line(DISPLAYSURF,BLACK,(200,i),(1760,i),4)





while True : 
	for event in pygame.event.get() :
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()