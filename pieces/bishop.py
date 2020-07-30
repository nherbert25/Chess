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