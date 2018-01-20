import sys , pygame
from pygame.locals import *


class Utils : 

	BLACK = (0,0,0)
	WHITE = (255,255,255)
	DISPLAYSURF = None

	def __init__(self,DISPLAYSURF):
		self.DISPLAYSURF = DISPLAYSURF


	def dwnImg(self) :
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

	def createText(self,text,x,y) :
		fontObj = pygame.font.Font('freesansbold.ttf', 32)
		textSurfaceObj = fontObj.render(text,True,self.BLACK)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (x,y)
		self.DISPLAYSURF.blit(textSurfaceObj,textRectObj)


	def setBoard (self,DISPLAYSURF,menuWidth,TOTALWIDTH,TOTALHEIGHT,cellWidth,cellInfoWidth,cellLineWidth,cellHeight) : 
		DISPLAYSURF = self.DISPLAYSURF
		boardCase = {}
		board = []
		compt = -1
		compt2 = 0
		# create the cell of the board 
		for i in range(menuWidth,TOTALWIDTH-cellInfoWidth,cellWidth) :
			cellLetter = ''
			cellNumber = ''
			compt +=1
			compt2 += 1 
			if compt2 == 1 :
				cellLetter = 'A' 
			if compt2 == 2 :
				cellLetter = 'B' 
			if compt2 == 3 :
			 	cellLetter = 'C'
			if compt2 == 4 :
				cellLetter = 'D'
			if compt2 == 5 :
				cellLetter = 'E'
			if compt2 == 6 :
				cellLetter = 'F'
			if compt2 == 7 :
				cellLetter = 'G' 
			if compt2 == 8 :
				cellLetter = 'H' 

			for j in range(0,TOTALHEIGHT-cellInfoWidth,cellHeight) :
				compt += 1

				if j == 0 :
					cellNumber = '8'
				if j == cellHeight :
					cellNumber = '7'
				if j == cellHeight*2 :
					cellNumber = '6'
				if j == cellHeight*3 :
					cellNumber = '5'
				if j == cellHeight*4 :
					cellNumber = '4'
				if j == cellHeight*5 :
					cellNumber = '3'
				if j == cellHeight*6 :
					cellNumber = '2'
				if j == cellHeight*7 :
					cellNumber = '1'

				if compt%2 == 0 :
					background = 0
				else :
					background = 1

				boardCase[cellLetter+cellNumber] = pygame.draw.rect(DISPLAYSURF, self.BLACK, (i,j, cellWidth, cellHeight),background)
		 #create the coordiantes (a1,h8 etc ...)
		for i in range(0,8*9,9) :
			if i == 0 :
				self.createText('8',boardCase['A8'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2)),boardCase['A8'].height/2)
				self.createText('A',boardCase['A8'].width/2+menuWidth,boardCase['A8'].top+(TOTALHEIGHT-(cellInfoWidth/2)))
			if i == 9 :
				self.createText('7',boardCase['B7'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth,boardCase['B7'].height/2+boardCase['B7'].top)
				self.createText('B',boardCase['B7'].width/2+boardCase['B7'].left,boardCase['B7'].top+(TOTALHEIGHT-(cellInfoWidth/2))-boardCase['B7'].top)
			if i == 18 :
				self.createText('6',boardCase['C6'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*2,boardCase['C6'].height/2+boardCase['C6'].top)
				self.createText('C',boardCase['C6'].width/2+boardCase['C6'].left,boardCase['C6'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*2)
			if i == 27 :
				self.createText('5',boardCase['D5'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*3,boardCase['D5'].height/2+boardCase['D5'].top)
				self.createText('D',boardCase['D5'].width/2+boardCase['D5'].left,boardCase['D5'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*3)
			if i == 36 :
				self.createText('4',boardCase['E4'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*4,boardCase['E4'].height/2+boardCase['E4'].top)
				self.createText('E',boardCase['E4'].width/2+boardCase['E4'].left,boardCase['E4'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*4)
			if i == 45 :
				self.createText('3',boardCase['F3'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*5,boardCase['F3'].height/2+boardCase['F3'].top)
				self.createText('F',boardCase['F3'].width/2+boardCase['F3'].left,boardCase['F3'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*5)
			if i == 54 :
				self.createText('2',boardCase['G2'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*6,boardCase['G2'].height/2+boardCase['G2'].top)
				self.createText('G',boardCase['G2'].width/2+boardCase['G2'].left,boardCase['G2'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*6)
			if i == 63 :
				self.createText('1',boardCase['H1'].left+(TOTALWIDTH-menuWidth-(cellInfoWidth/2))-cellWidth*7,boardCase['H1'].height/2+boardCase['H1'].top)
				self.createText('H',boardCase['H1'].width/2+boardCase['H1'].left,boardCase['H1'].top+(TOTALHEIGHT-(cellInfoWidth/2))-cellHeight*7)