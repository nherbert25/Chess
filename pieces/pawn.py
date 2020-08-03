from pieces.piece import Piece

class Pawn(Piece):

	alliance = None
	position = None
	name = 'pawn'
	moved = False
	original_square = None
	canPromote = True
	
	def __init__(self, alliance, position):
		Piece.__init__(self, alliance)
		self.alliance = alliance
		self.position = position
		self.original_square = position
		
	def toString(self):
		return("P" if self.alliance == "Black" else "p")

	def movement(self, original_position):
		alliance = self.alliance
		moved = self.moved
		potential_legal_moves = []
		if original_position != self.original_square:
			moved = True

		potential_legal_moves.append([])
		if alliance == 'White' and original_position-8 >= 0:
			potential_legal_moves[0].append(original_position-8)
			if moved == False and original_position-16 >= 0:
				potential_legal_moves[0].append(original_position-16)
		if alliance == 'Black' and original_position+8 <= 63:
			potential_legal_moves[0].append(original_position+8)
			if moved == False and original_position+16 <= 63:
				potential_legal_moves[0].append(original_position+16)

		potential_legal_moves.append([])
		if alliance == 'White' and original_position-9 >= 0 and original_position%8 > (original_position-1)%8:
			potential_legal_moves[1].append(original_position-9)
		if alliance == 'Black' and original_position+9 <= 63 and original_position%8 < (original_position+1)%8:
			potential_legal_moves[1].append(original_position+9)
		if alliance == 'White' and original_position-7 >= 0 and original_position%8 < (original_position+1)%8:
			potential_legal_moves[1].append(original_position-7)
		if alliance == 'Black' and original_position+7 <= 63 and original_position%8 > (original_position-1)%8:
			potential_legal_moves[1].append(original_position+7)
		
		return(potential_legal_moves)