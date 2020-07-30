from pieces.piece import Piece

class Knight(Piece):

	alliance = None
	position = None
	
	def __init__(self, alliance, position):
		Piece.__init__(self, alliance)
		self.alliance = alliance
		self.position = position
		
	def toString(self):
		return("N" if self.alliance == "Black" else "n")

	def movement(self, original_position):
		potential_legal_moves = []

		test_position = original_position - 17
		if test_position >= 0 and test_position % 8 < original_position % 8:
			potential_legal_moves.append(test_position)
		test_position = original_position - 15
		if test_position >= 0 and test_position % 8 > original_position % 8:
			potential_legal_moves.append(test_position)
		test_position = original_position - 10
		if test_position >= 0 and test_position % 8 < original_position % 8:
			potential_legal_moves.append(test_position)
		test_position = original_position - 6
		if test_position >= 0 and test_position % 8 > original_position % 8:
			potential_legal_moves.append(test_position)
		test_position = original_position + 6
		if test_position <= 63 and test_position % 8 < original_position % 8:
			potential_legal_moves.append(test_position)
		test_position = original_position + 10
		if test_position <= 63 and test_position % 8 > original_position % 8:
			potential_legal_moves.append(test_position)
		test_position = original_position + 15
		if test_position <= 63 and test_position % 8 < original_position % 8:
			potential_legal_moves.append(test_position)
		test_position = original_position + 17
		if test_position <= 63 and test_position % 8 > original_position % 8:
			potential_legal_moves.append(test_position)

		return(potential_legal_moves)
