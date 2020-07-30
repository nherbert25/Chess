from pieces.piece import Piece

class Queen(Piece):

	alliance = None
	position = None
	name = 'queen'
	
	def __init__(self, alliance, position):
		Piece.__init__(self, alliance)
		self.alliance = alliance
		self.position = position
		
	def toString(self):
		return("Q" if self.alliance == "Black" else "q")

	def movement(self, original_position):
		potential_legal_moves = []

		potential_legal_moves.append([])
		test_position = original_position-1
		while test_position%8 < original_position % 8:
			potential_legal_moves[0].append(test_position)
			test_position -= 1

		potential_legal_moves.append([])
		test_position = original_position+1
		while test_position%8 > original_position % 8:
			potential_legal_moves[1].append(test_position)
			test_position += 1

		potential_legal_moves.append([])
		test_position = original_position-8
		while test_position >= 0:
			potential_legal_moves[2].append(test_position)
			test_position -= 8

		potential_legal_moves.append([])
		test_position = original_position+8
		while test_position <= 63:
			potential_legal_moves[3].append(test_position)
			test_position += 8

		potential_legal_moves.append([])
		test_position = original_position-9
		while test_position >= 0 and test_position % 8 < original_position % 8:
			potential_legal_moves[4].append(test_position)
			test_position -= 9

		potential_legal_moves.append([])
		test_position = original_position-7
		while test_position >= 0 and test_position % 8 > original_position % 8:
			potential_legal_moves[5].append(test_position)
			test_position -= 7

		potential_legal_moves.append([])
		test_position = original_position+9
		while test_position <= 63 and test_position % 8 > original_position % 8:
			potential_legal_moves[6].append(test_position)
			test_position += 9

		potential_legal_moves.append([])
		test_position = original_position+7
		while test_position <= 63 and test_position % 8 < original_position % 8:
			potential_legal_moves[7].append(test_position)
			test_position += 7

		return(potential_legal_moves)