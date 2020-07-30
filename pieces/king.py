from pieces.piece import Piece

class King(Piece):

	alliance = None
	position = None
	name = 'king'
	
	def __init__(self, alliance, position):
		Piece.__init__(self, alliance)
		self.alliance = alliance
		self.position = position
		
	def toString(self):
		return("K" if self.alliance == "Black" else "k")