#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from pygame import transform


# classe de stockage des variables et fonction necessitant ses variables
class Data :
	pwnFirstMove = []



	def __init__(self,TOTALWIDTH,TOTALHEIGHT,DISPLAYSURF) :
		self.TOTALWIDTH = TOTALWIDTH
		self.TOTALHEIGHT = TOTALHEIGHT
		self.BLACK = (0,0,0)
		self.WHITE = (255,255,255)
		self.cellInfoWidth = 40
		self.cellLineWidth = 4
		self.menuWidth = self.TOTALWIDTH/10
		self.cellWidth = (self.TOTALWIDTH-self.menuWidth-self.cellInfoWidth)/8
		self.cellHeight = int(math.ceil(float((self.TOTALHEIGHT-self.cellInfoWidth))/8))
		self.DISPLAYSURF = DISPLAYSURF

	#met une image à la taille des cellules puis dans les cellules données en destination
	def cellScaling(self,givObj,*destinations) :
		givObjs = []
		i = 0
		for destination in destinations :
			givObjs.append(self.DISPLAYSURF.blit( transform.scale(givObj,(destination.width-1,destination.height-1)), destination))
			i += 1
		return givObjs