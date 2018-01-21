#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys , pygame , logUtil
from pygame.locals import *
from PIL import Image




BLACK = (0,0,0)
WHITE = (255,255,255)
BROWN = (146,98,57)
logger = logUtil.LogUtil()

#charge toutes les images des pieces du jeu
def dwnImg() :
	pieces = {
		'white_queen' : pygame.image.load('img/white_queen.png'),
		'white_rook' : pygame.image.load('img/white_rook.png'),
		'white_bishop' : pygame.image.load('img/white_bishop.png'),
		'white_pawn' : pygame.image.load('img/white_pawn.png'),
		'white_knight' : pygame.image.load('img/white_knight.png'),
		'black_queen' : pygame.image.load('img/black_queen.png'),
		'black_king' : pygame.image.load('img/black_king.png'),
		'black_rook' : pygame.image.load('img/black_rook.png'),
		'black_bishop' : pygame.image.load('img/black_bishop.png'),
		'black_pawn' : pygame.image.load('img/black_pawn.png'),
		'black_knight' : pygame.image.load('img/black_knight.png'),
		'white_king' : pygame.image.load('img/white_king.png')
	}

	return pieces

#creer un text en noir taille 32 en x,y
def createText(DISPLAYSURF,text,x,y) :
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfaceObj = fontObj.render(text,True,BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x,y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)


#creer le damier 
def setBoard (DISPLAYSURF,menuWidth,TOTALWIDTH,TOTALHEIGHT,cellWidth,cellInfoWidth,cellLineWidth,cellHeight) : 
	boardCase = {}
	compt = -1
	compt2 = 0
	# create the cell of the board 
	for i in xrange(menuWidth,TOTALWIDTH-cellInfoWidth,cellWidth) :
		cellNumber = ''
		compt +=1
		compt2 += 1 
		#transform number in alphabetical uppercase letter
		cellLetter = chr(compt2+0x40)

		for j in xrange(0,TOTALHEIGHT-cellInfoWidth,cellHeight) :
			compt += 1
			cellNumber = str(8-(j/cellHeight))

			if compt%2 == 0 :
				background = 0
			else :
				background = 1

			boardCase[cellLetter+cellNumber] = pygame.draw.rect(DISPLAYSURF, BROWN, (i,j, cellWidth, cellHeight),background)
			if cellNumber == '1' :
				break

		if cellLetter =='H' :
				break
	#create the coordiantes (a1,h8 etc ...)
	for i in xrange(0,8*9,9) :
		if i == 0 :
			createText(DISPLAYSURF,'8',boardCase['A8'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2)),boardCase['A8'].height/2)
			createText(DISPLAYSURF,'A',boardCase['A8'].width/2+menuWidth,boardCase['A8'].top+(TOTALHEIGHT-(cellInfoWidth/2)))
		if i == 9 :
			createText(DISPLAYSURF,'7',boardCase['B7'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth,boardCase['B7'].height/2+boardCase['B7'].top)
			createText(DISPLAYSURF,'B',boardCase['B7'].width/2+boardCase['B7'].left,boardCase['B7'].top+(TOTALHEIGHT-(cellInfoWidth/2))-boardCase['B7'].top)
		if i == 18 :
			createText(DISPLAYSURF,'6',boardCase['C6'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*2,boardCase['C6'].height/2+boardCase['C6'].top)
			createText(DISPLAYSURF,'C',boardCase['C6'].width/2+boardCase['C6'].left,boardCase['C6'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*2)
		if i == 27 :
			createText(DISPLAYSURF,'5',boardCase['D5'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*3,boardCase['D5'].height/2+boardCase['D5'].top)
			createText(DISPLAYSURF,'D',boardCase['D5'].width/2+boardCase['D5'].left,boardCase['D5'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*3)
		if i == 36 :
			createText(DISPLAYSURF,'4',boardCase['E4'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*4,boardCase['E4'].height/2+boardCase['E4'].top)
			createText(DISPLAYSURF,'E',boardCase['E4'].width/2+boardCase['E4'].left,boardCase['E4'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*4)
		if i == 45 :
			createText(DISPLAYSURF,'3',boardCase['F3'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*5,boardCase['F3'].height/2+boardCase['F3'].top)
			createText(DISPLAYSURF,'F',boardCase['F3'].width/2+boardCase['F3'].left,boardCase['F3'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*5)
		if i == 54 :
			createText(DISPLAYSURF,'2',boardCase['G2'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*6,boardCase['G2'].height/2+boardCase['G2'].top)
			createText(DISPLAYSURF,'G',boardCase['G2'].width/2+boardCase['G2'].left,boardCase['G2'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*6)
		if i == 63 :
			createText(DISPLAYSURF,'1',boardCase['H1'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*7,boardCase['H1'].height/2+boardCase['H1'].top)
			createText(DISPLAYSURF,'H',boardCase['H1'].width/2+boardCase['H1'].left,boardCase['H1'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*7)

	return boardCase


#met les images des pieces a leurs places de départs et renvoie le dictionnaire avec ses positions
def setPieces(boardCase,gameData) :
	pieces = dwnImg()
	piecesDict = {}
	for piece in pieces :
		if piece == 'white_queen' :
			piecesDict['white_queen'] = gameData.cellScaling(pieces[piece],boardCase['D1'])[0]
		if piece == 'white_rook' :
			iterator = gameData.cellScaling(pieces[piece],boardCase['H1'],boardCase['A1'])
			for i in range(0,2) :
				piecesDict['white_rook'+str(i)] = iterator[i]
		if piece == 'white_bishop' :
			iterator = gameData.cellScaling(pieces[piece],boardCase['C1'],boardCase['F1'])
			for i in range(0,2) :
				piecesDict['white_bishop'+str(i)] = iterator[i]
		if piece == 'white_pawn' :
			iterator = gameData.cellScaling(pieces[piece],boardCase['A2'],boardCase['B2'],boardCase['C2'],boardCase['D2'],boardCase['E2'],boardCase['F2'],boardCase['G2'],boardCase['H2'])
			for i in range(0,8) :
				piecesDict['white_pawn'+str(i)] = iterator[i]
		if piece == 'white_knight' :
			iterator = gameData.cellScaling(pieces[piece],boardCase['B1'],boardCase['G1'])
			for i in range(0,2) :
				piecesDict['white_knight'+str(i)] = iterator[i]
		if piece == 'black_queen' :
			piecesDict['black_queen'] = gameData.cellScaling(pieces[piece],boardCase['D8'])[0]
		if piece == 'black_king' :
			piecesDict['black_king'] = gameData.cellScaling(pieces[piece],boardCase['E8'])[0]
		if piece == 'black_rook' :
			iterator = gameData.cellScaling(pieces[piece],boardCase['H8'],boardCase['A8'])
			for i in range(0,2) :
				piecesDict['black_rook'+str(i)] = iterator[i]
		if piece == 'black_bishop' :
			iterator = gameData.cellScaling(pieces[piece],boardCase['C8'],boardCase['F8'])
			for i in range(0,2) :
				piecesDict['black_bishop'+str(i)] = iterator[i]
		if piece == 'black_pawn' :
			iterator = gameData.cellScaling(pieces[piece],boardCase['A7'],boardCase['B7'],boardCase['C7'],boardCase['D7'],boardCase['E7'],boardCase['F7'],boardCase['G7'],boardCase['H7'])
			for i in range(0,8) :
				piecesDict['black_pawn'+str(i)] = iterator[i]
		if piece == 'black_knight' :
			iterator = gameData.cellScaling(pieces[piece],boardCase['B8'],boardCase['G8'])
			for i in range(0,2) :
				piecesDict['black_knight'+str(i)] = iterator[i]
		if piece == 'white_king' :
			piecesDict['white_king'] = gameData.cellScaling(pieces[piece],boardCase['E1'])[0]
	return piecesDict

#trouve le Rect sur lequel on a cliqué
def findRect(posx,posy,dico) :
	for element in dico :
		if dico[element].left < posx and posx < dico[element].right  and dico[element].top < posy  and  posy < dico[element].bottom :
			return element, dico[element]
	return None,None


#met les images des pieces au bonne endroit après les mouvement grace au dictionnaire des pieces
def refreshPieces(dico,gameData) :
	imgs = dwnImg()
	for piece in dico :
		if piece == 'white_king' or piece == 'black_king' or piece == 'white_queen' or piece == 'black_queen' :
			gameData.cellScaling(imgs[piece],dico[piece])
		else :
			stub = piece[:-1]
			gameData.cellScaling(imgs[stub],dico[piece])



#classe qui donnent les cases ou peut aller une piece
#classe a finir seulement les pionts de commencés et manque la verif de si il y a un adversaire dans les diagonales
def allowedMvnt(pieceName,cellName,piecesDict,FM,board) :
	allowedCell = []
	colorSign = 1 if 'white' in pieceName else -1
	color = 'white' if 'white' in pieceName else 'black'
		
	if 'pawn' in pieceName :
		towardCell = cellName[0]+str(int(cellName[1])+colorSign)
		x,y = board[towardCell].left+10 , board[towardCell].top+10
		if findRect(x,y,piecesDict) == (None,None) :
			allowedCell.append(towardCell)
		
		if pieceName not in FM :
			allowedCell.append(cellName[0]+str(int(cellName[1])+2*colorSign))

		offensedCell = [chr(ord(cellName[0])+1)+str(int(cellName[1])+colorSign),chr(ord(cellName[0])-1)+str(int(cellName[1])+colorSign)]
		if '@' not in offensedCell[0] and 'I' not in offensedCell[0] :
			x,y = board[offensedCell[0]].left+10 , board[offensedCell[0]].top+10
			attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
			if  attackedPieceName != None and color not in attackedPieceName :
				allowedCell.append(offensedCell[0])
				
		if  '@' not in offensedCell[1] and 'I' not in offensedCell[1] :
			x,y = board[offensedCell[1]].left+10 , board[offensedCell[1]].top+10
			attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
			if  attackedPieceName != None and color not in attackedPieceName :
				allowedCell.append(offensedCell[1])

		return allowedCell

	if 'rook' in pieceName or 'queen' in pieceName:
		#regarde les cases libres au dessus
		for i in xrange(1,8) :
			towardCell = cellName[0]+str(int(cellName[1])+i)
			if towardCell in board :
				x,y = board[towardCell].left+10 , board[towardCell].top+10
				attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
				if  attackedPieceName != None and color in attackedPieceName :
					break
				else :
					allowedCell.append(towardCell)
					if attackedPieceName != None :
						break
		#regarde les cases libres en dessous
		for i in xrange(-1,-8,-1) :
			towardCell = cellName[0]+str(int(cellName[1])+i)
			if towardCell in board :
				x,y = board[towardCell].left+10 , board[towardCell].top+10
				attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
				if  attackedPieceName != None and color in attackedPieceName :
					break
				else :
					allowedCell.append(towardCell)
					if attackedPieceName != None :
						break

		#regarde les cases libres a gauche
		for i in xrange(1,8) :
			towardCell = chr(ord(cellName[0])+i)+cellName[1]
			if towardCell in board :
				x,y = board[towardCell].left+10 , board[towardCell].top+10
				attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
				if  attackedPieceName != None and color in attackedPieceName :
					break
				else :
					allowedCell.append(towardCell)
					if attackedPieceName != None :
						break

		#regarde les cases libres a droite
		for i in xrange(-1,-8,-1) :
			towardCell = chr(ord(cellName[0])+i)+cellName[1]
			if towardCell in board :
				x,y = board[towardCell].left+10 , board[towardCell].top+10
				attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
				if  attackedPieceName != None and color in attackedPieceName :
					break
				else :
					allowedCell.append(towardCell)
					if attackedPieceName != None :
						break

		return allowedCell

	if 'bishop' in pieceName or 'queen' in pieceName :
		#regarde les cases libres en diago haut droit
		for i in xrange(1,8) :
			towardCell = chr(ord(cellName[0])+i)+str(int(cellName[1])+i)
			if towardCell in board :
				x,y = board[towardCell].left+10 , board[towardCell].top+10
				attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
				if  attackedPieceName != None and color in attackedPieceName :
					break
				else :
					allowedCell.append(towardCell)
					if attackedPieceName != None :
						break
		#regarde les cases libres en diago bas gauche ###
		for i in xrange(-1,-8,-1) :
			towardCell = chr(ord(cellName[0])+i)+str(int(cellName[1])+i)
			if towardCell in board :
				x,y = board[towardCell].left+10 , board[towardCell].top+10
				attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
				if  attackedPieceName != None and color in attackedPieceName :
					break
				else :
					allowedCell.append(towardCell)
					if attackedPieceName != None :
						break
		#regarde les cases libres en diago bas droite
		for i in xrange(1,8) :
			towardCell = chr(ord(cellName[0])+i)+str(int(cellName[1])-i)
			if towardCell in board :
				x,y = board[towardCell].left+10 , board[towardCell].top+10
				attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
				if  attackedPieceName != None and color in attackedPieceName :
					break
				else :
					allowedCell.append(towardCell)
					if attackedPieceName != None :
						break
		#regarde les cases libres en diago haut gauche
		for i in xrange(1,8) :
			towardCell = chr(ord(cellName[0])-i)+str(int(cellName[1])+i)
			if towardCell in board :
				x,y = board[towardCell].left+10 , board[towardCell].top+10
				attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
				if  attackedPieceName != None and color in attackedPieceName :
					break
				else :
					allowedCell.append(towardCell)
					if attackedPieceName != None :
						break

		return allowedCell

	if 'knight' in pieceName :
		towardCell = chr(ord(cellName[0])+1)+str(int(cellName[1])+2)
		allowedCell = nonAllyCell(allowedCell,towardCell,board,piecesDict,color)

		towardCell = chr(ord(cellName[0])+2)+str(int(cellName[1])+1)
		allowedCell = nonAllyCell(allowedCell,towardCell,board,piecesDict,color)

		towardCell = chr(ord(cellName[0])-1)+str(int(cellName[1])+2)
		allowedCell = nonAllyCell(allowedCell,towardCell,board,piecesDict,color)

		towardCell = chr(ord(cellName[0])+1)+str(int(cellName[1])-2)
		allowedCell = nonAllyCell(allowedCell,towardCell,board,piecesDict,color)

		towardCell = chr(ord(cellName[0])-1)+str(int(cellName[1])-2)
		allowedCell = nonAllyCell(allowedCell,towardCell,board,piecesDict,color)

		towardCell = chr(ord(cellName[0])-2)+str(int(cellName[1])+1)
		allowedCell = nonAllyCell(allowedCell,towardCell,board,piecesDict,color)

		towardCell = chr(ord(cellName[0])+2)+str(int(cellName[1])-1)
		allowedCell = nonAllyCell(allowedCell,towardCell,board,piecesDict,color)

		towardCell = chr(ord(cellName[0])-2)+str(int(cellName[1])-1)
		allowedCell = nonAllyCell(allowedCell,towardCell,board,piecesDict,color)

		return allowedCell

	if 'king' in pieceName :
		for j in range (-1,2,1) :
			for i in range(-1,2,1) :
				towardCell = chr(ord(cellName[0])+j)+str(int(cellName[1])+i)
				if towardCell != cellName:
					allowedCell = nonAllyCell(allowedCell,towardCell,board,piecesDict,color)

		return allowedCell	

	return allowedCell


def nonAllyCell(listMvt,cell,board,piecesDict,colorPiece) :
	if cell in board :
		x,y = board[cell].left+10 , board[cell].top+10
		attackedPieceName,attackedPieceObj = findRect(x,y,piecesDict)
		if  attackedPieceName == None or colorPiece not in attackedPieceName :
			listMvt.append(cell)
	return listMvt

