#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
	gameData = data.Data(TOTALWIDTH,TOTALHEIGHT,DISPLAYSURF)
	pygame.display.set_caption("chess")

	#variable a envoyer dans gameData
	mouse_x =0
	mouse_y =0
	isClicked = False
	selectedPieceObj = None
	selectedPieceName = None
	selectedCellName = None
	selectedCellObj = None
	colorTurn = 'white'

	#initiate Utils
	logger = logUtil.LogUtil()


	# initiate the chess board	
	DISPLAYSURF.fill(gameData.WHITE)
	board = utils.setBoard (DISPLAYSURF,gameData.menuWidth,gameData.TOTALWIDTH,gameData.TOTALHEIGHT,gameData.cellWidth,gameData.cellInfoWidth,gameData.cellLineWidth,gameData.cellHeight)
	pieces = utils.setPieces(board,gameData)

	#boucle principale du jeu
	while True : 

		#rafraichissement du plateau 
		DISPLAYSURF.fill(gameData.WHITE)
		board = utils.setBoard (DISPLAYSURF,gameData.menuWidth,gameData.TOTALWIDTH,gameData.TOTALHEIGHT,gameData.cellWidth,gameData.cellInfoWidth,gameData.cellLineWidth,gameData.cellHeight)
		if selectedCellObj != None :
			pygame.draw.rect(DISPLAYSURF,(30,144,255), (selectedCellObj.left,selectedCellObj.top, gameData.cellWidth, gameData.cellHeight))
		utils.refreshPieces(pieces,gameData)
		pygame.display.flip()

		#recuperation des events
		for event in pygame.event.get() :
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			#au click
			elif event.type == MOUSEBUTTONUP :
			 	if event.button == 1 :
			 		mouse_x,mouse_y = event.pos
			 		#premier click mise en mémoire de la pièce sélectionée
			 		if isClicked == False :
				 		clickedPieceName,clickedPieceObj = utils.findRect(mouse_x,mouse_y,pieces)
				 		clickedCellName,clickedCellObj = utils.findRect(mouse_x,mouse_y,board)
				 		if clickedPieceName != None and  colorTurn in clickedPieceName:
				 			isClicked = True
				 			selectedPieceObj = clickedPieceObj
				 			selectedPieceName = clickedPieceName
				 			selectedCellName = clickedCellName
				 			selectedCellObj = clickedCellObj

				 			clickedPieceObj = None
				 			clickedPieceName = None
				 	#deuxième click
				 	else :
				 		targetCellName,targetCellObj = utils.findRect(mouse_x,mouse_y,board)
				 		targetPieceName,targetPieceObj = utils.findRect(mouse_x,mouse_y,pieces)
				 		allowedCell = utils.allowedMvnt(selectedPieceName,selectedCellName,pieces,gameData.pwnFirstMove,board)
				 		logger.logPrinter(allowedCell)
				 		if targetCellName in allowedCell :
					 		if targetCellName != None :
					 			pieces[selectedPieceName] = targetCellObj

					 			#capture du premier mouvement 
					 			if 'pawn' in selectedPieceName and selectedPieceName not in gameData.pwnFirstMove :
					 				gameData.pwnFirstMove.append(selectedPieceName)
					 			if 'king' in selectedPieceName and selectedPieceName not in gameData.pwnFirstMove :
					 				gameData.pwnFirstMove.append(selectedPieceName)
					 			if 'rook' in selectedPieceName and selectedPieceName not in gameData.pwnFirstMove :
					 				gameData.pwnFirstMove.append(selectedPieceName)
					 			#color qui doit jouer
					 			if colorTurn == 'white' :
				 					colorTurn = 'black'
				 				else :
				 					colorTurn = 'white'
				 			# piece mangée
					 		if targetPieceName != None :
					 			pieces.pop(targetPieceName,None)

					 	#reset du click
				 		isClicked = False
				 		targetCellName = None
				 		selectedPieceObj = None
				 		selectedPieceName = None
				 		selectedCellName = None
				 		selectedCellObj = None


#width et height de l'ecran a passer en parametre
if __name__ == '__main__':
	parser = ArgumentParser(description = 'A chess game from Sleet04')
	parser.add_argument('TOTALWIDTH',help='width of the screen',type=int)
	parser.add_argument('TOTALHEIGHT',help='width of the screen',type=int)
	args = parser.parse_args()
	__initiateGame__(args.TOTALWIDTH,args.TOTALHEIGHT)
	