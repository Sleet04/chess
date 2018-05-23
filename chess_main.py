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
	inCheck = False
	END_OF_GAME="this is the end" 

	#initiate Utils
	logger = logUtil.LogUtil()


	# initiate the chess board	
	DISPLAYSURF.fill(gameData.WHITE)
	board = utils.setBoard (DISPLAYSURF,gameData.menuWidth,gameData.TOTALWIDTH,gameData.TOTALHEIGHT,gameData.cellWidth,gameData.cellInfoWidth,gameData.cellLineWidth,gameData.cellHeight)
	pieces = utils.setPieces(board,gameData)
	if inCheck == True :
		utils.createText(DISPLAYSURF,'chess',10,10)

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
				 		allowedCell = utils.allowedMvnt(selectedPieceName,selectedCellName,pieces,gameData.firstMove,board)
				 		oldPieces = pieces.copy()
				 		if targetCellName in allowedCell :
					 		if targetCellName != None :
					 			
					 			#rock management
					 			if 'king' in selectedPieceName and selectedPieceName not in gameData.firstMove :
					 				if selectedPieceName == 'white_king' and ( targetCellName == 'H1' or targetCellName == 'A1') :
						 				tempVar = selectedCellObj
						 				pieces[selectedPieceName] = targetCellObj
						 				pieces[targetPieceName] = tempVar
						 				targetPieceName = None
						 			elif selectedPieceName == 'black_king' and ( targetCellName == 'H8' or targetCellName == 'A8') :
						 				tempVar = selectedCellObj
						 				pieces[selectedPieceName] = targetCellObj
						 				pieces[targetPieceName] = tempVar
						 				targetPieceName = None
					 				else : 
					 					pieces[selectedPieceName] = targetCellObj
					 			else : 
					 					pieces[selectedPieceName] = targetCellObj


					 			#capture du premier mouvement 
					 			if 'pawn' in selectedPieceName and selectedPieceName not in gameData.firstMove :
					 				gameData.firstMove.append(selectedPieceName)
					 			if 'king' in selectedPieceName and selectedPieceName not in gameData.firstMove :
					 				gameData.firstMove.append(selectedPieceName)
					 			if 'rook' in selectedPieceName and selectedPieceName not in gameData.firstMove :
					 				gameData.firstMove.append(selectedPieceName)

					 			king = colorTurn+'_king'
						 		kingCell, uselessVar = utils.findRect(pieces[king].left+10,pieces[king].top+10,board)
						 		if utils.chess(board,pieces,kingCell,colorTurn,gameData.firstMove) == True :
						 			inCheck = True
						 			pieces = oldPieces
						 			targetPieceName = None
						 		else :
					 			#color qui doit jouer
					 				inCheck = False
						 			if colorTurn == 'white' :
					 					colorTurn = 'black'
					 				else :
					 					colorTurn = 'white'

					 			if utils.chess(board,pieces,kingCell,colorTurn,gameData.firstMove) == True :
					 				ouf = False
					 				for piece in pieces :
					 					if colorTurn in piece :
						 					pieceCellName,pieceCellRect = utils.findRect(pieces[piece].left+5,pieces[piece].top+5,board)
						 					allowedCell = utils.allowedMvnt(piece,pieceCellName,pieces,gameData.firstMove,board)
						 					for cells in allowedCell :
						 						tempPieces = pieces.copy()
						 						tempPieces[piece] = board[cells]
						 						if utils.chess(board,tempPieces,kingCell,colorTurn,gameData.firstMove) == False :
						 							ouf = True
						 			if ouf == False :
						 				utils.createText(DISPLAYSURF,END_OF_GAME,0,0)
						 				print "end of game"				

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
	