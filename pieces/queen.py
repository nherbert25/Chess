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