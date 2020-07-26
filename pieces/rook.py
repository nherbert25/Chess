from pieces.piece import Piece

class Rook(Piece):

	alliance = None
	position = None
	
	def __init__(self, alliance, position):
		self.alliance = alliance
		self.position = position
		
	def toString(self):
		return("R" if self.alliance == "Black" else "r")

	def movement(self):
		alliance = self.alliance
		original_position = self.position
		legal_moves = []
		

		if original_position % 8 != 0:
			test_position = original_position-1
			while test_position%7 != 0:
				legal_moves.append(test_position)
				test_position -= 1

		test_position = original_position+1
		while test_position%8 != 0:
			legal_moves.append(test_position)
			test_position += 1

		test_position = original_position-8
		while test_position > 0:
			legal_moves.append(test_position)
			test_position -= 8
		
		test_position = original_position+8
		while test_position < 64:
			legal_moves.append(test_position)
			test_position += 8
		#return legal squares
		return(legal_moves)