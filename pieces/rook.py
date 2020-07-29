from pieces.piece import Piece
import pygame

class Rook(Piece):


	def __init__(self, alliance, position):
		Piece.__init__(self, alliance)
		self.alliance = alliance
		self.position = position

		#print(self.sprite, self.alliance, self.position)
		
	def toString(self):
		return("R" if self.alliance == "Black" else "r")

	def movement(self, original_position):
		potential_legal_moves = []

		if original_position % 8 != 0:
			test_position = original_position-1
			while test_position%8 != 0:
				potential_legal_moves.append(test_position)
				test_position -= 1
			potential_legal_moves.append(test_position)

		test_position = original_position+1
		while test_position%8 != 0:
			potential_legal_moves.append(test_position)
			test_position += 1

		test_position = original_position-8
		while test_position >= 0:
			potential_legal_moves.append(test_position)
			test_position -= 8
		
		test_position = original_position+8
		while test_position < 64:
			potential_legal_moves.append(test_position)
			test_position += 8
		#return legal squares
		return(potential_legal_moves)

'''
	def movement(self, original_position):
		potential_legal_moves = []

		if original_position % 8 != 0:
			test_position = original_position-1
			while test_position%8 != 0:
				potential_legal_moves.append(test_position)
				test_position -= 1
			potential_legal_moves.append(test_position)

		test_position = original_position+1
		while test_position%8 != 0:
			potential_legal_moves.append(test_position)
			test_position += 1

		test_position = original_position-8
		while test_position >= 0:
			potential_legal_moves.append(test_position)
			test_position -= 8
		
		test_position = original_position+8
		while test_position < 64:
			potential_legal_moves.append(test_position)
			test_position += 8
		#return legal squares
		return(potential_legal_moves)
	
'''