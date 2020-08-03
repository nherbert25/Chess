import pygame

class Piece:

	alliance = None
	position = None
	sprite = None
	name = None
	can_promote = False
	has_moved = False

	def __init__(self, alliance):
		self.sprite = "./ChessArt/"+alliance[0].upper()+self.toString().upper()+".png"

	def movement(self, position):
		pass
	
	def toString(self):
		pass