import sys , pygame , logUtil
from pygame.locals import *




BLACK = (0,0,0)
WHITE = (255,255,255)
DISPLAYSURF = None
logger = logUtil.LogUtil()


def dwnImg() :
	pieces = {
		'white_queen' : pygame.image.load('img/white_queen.png'),
		'white_king' : pygame.image.load('img/white_king.png'),
		'white_rook' : pygame.image.load('img/white_rook.png'),
		'white_bishop' : pygame.image.load('img/white_bishop.png'),
		'white_pawn' : pygame.image.load('img/white_pawn.png'),
		'white_knight' : pygame.image.load('img/white_knight.png'),
		'black_queen' : pygame.image.load('img/black_queen.png'),
		'black_king' : pygame.image.load('img/black_king.png'),
		'black_rook' : pygame.image.load('img/black_rook.png'),
		'black_bishop' : pygame.image.load('img/black_bishop.png'),
		'black_pawn' : pygame.image.load('img/black_pawn.png'),
		'black_knight' : pygame.image.load('img/black_knight.png')
	}
	return pieces

def createText(DISPLAYSURF,text,x,y) :
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfaceObj = fontObj.render(text,True,BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (x,y)
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)


def setBoard (DISPLAYSURF,menuWidth,TOTALWIDTH,TOTALHEIGHT,cellWidth,cellInfoWidth,cellLineWidth,cellHeight) : 
	DISPLAYSURF = DISPLAYSURF
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

			boardCase[cellLetter+cellNumber] = pygame.draw.rect(DISPLAYSURF, BLACK, (i,j, cellWidth, cellHeight),background)
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


def setPieces(DISPLAYSURF ,boardCase) :
	pieces = dwnImg()
	for piece in pieces :
		if piece == 'white_queen' :
			pieces[piece] = pygame.transform.scale(pieces[piece],(boardCase['D1'].width,boardCase['D1'].height))
			DISPLAYSURF.blit( pieces[piece], boardCase['D1'])

		# if piece == 'white_king' :

		# if piece == 'white_rook' :

		# if piece == 'white_bishop' :

		# if piece == 'white_pawn' :

		# if piece == 'white_knight' :

		# if piece == 'black_queen' :

		# if piece == 'black_king' :

		# if piece == 'black_rook' :

		# if piece == 'black_bishop' :

		# if piece == 'black_pawn' :

		# if piece == 'black_knight' :

# def cellScaling() :
