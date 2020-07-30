from pieces.piece import Piece

class Bishop(Piece):

	alliance = None
	position = None
	name = 'bishop'
	
	def __init__(self, alliance, position):
		Piece.__init__(self, alliance)
		self.alliance = alliance
		self.position = position
		
	def toString(self):
		return("B" if self.alliance == "Black" else "b")

	def movement(self, original_position):
		potential_legal_moves = []

		potential_legal_moves.append([])
		test_position = original_position-9
		while test_position >= 0 and test_position % 8 < original_position % 8:
			potential_legal_moves[0].append(test_position)
			test_position -= 9

		potential_legal_moves.append([])
		test_position = original_position-7
		while test_position >= 0 and test_position % 8 > original_position % 8:
			potential_legal_moves[1].append(test_position)
			test_position -= 7

		potential_legal_moves.append([])
		test_position = original_position+9
		while test_position <= 63 and test_position % 8 > original_position % 8:
			potential_legal_moves[0].append(test_position)
			test_position += 9

		potential_legal_moves.append([])
		test_position = original_position+7
		while test_position <= 63 and test_position % 8 < original_position % 8:
			potential_legal_moves[0].append(test_position)
			test_position += 7

		#return legal squares
		print(potential_legal_moves)
		return(potential_legal_moves)