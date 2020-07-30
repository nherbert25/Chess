import pygame

class Piece:

	alliance = None
	position = None
	sprite = None
	name = None

	def __init__(self, alliance):
		self.sprite = "./ChessArt/"+alliance[0].upper()+self.toString().upper()+".png"

	def movement(self, position):
		pass
	
	def toString(self):
		pass