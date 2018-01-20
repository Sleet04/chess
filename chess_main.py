import sys , pygame
from pygame.locals import *
import csv
import math 
import utils
import logUtil
from argparse import ArgumentParser
import data



def __initiateGame__(TOTALWIDTH,TOTALHEIGHT) :
	

	#initiate the UI
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((TOTALWIDTH,TOTALHEIGHT))
	gameData = data.Data(TOTALWIDTH,TOTALHEIGHT)
	DISPLAYSURF.fill(WHITE)
	pygame.display.set_caption("chess")

	#initiate Utils
	logger = logUtil.LogUtil()


	# initiate the chess board
	board = utils.setBoard (DISPLAYSURF,menuWidth,TOTALWIDTH,TOTALHEIGHT,cellWidth,cellInfoWidth,cellLineWidth,cellHeight)
	utils.setPieces(DISPLAYSURF,board)

	while True : 
		for event in pygame.event.get() :
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()




if __name__ == '__main__':
	parser = ArgumentParser(description = 'A chess game from Sleet04')
	parser.add_argument('TOTALWIDTH',help='width of the screen',type=int)
	parser.add_argument('TOTALHEIGHT',help='width of the screen',type=int)
	args = parser.parse_args()
	__initiateGame__(args.TOTALWIDTH,args.TOTALHEIGHT)
	