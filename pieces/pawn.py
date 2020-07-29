from pieces.piece import Piece

class Pawn(Piece):

	alliance = None
	position = None
	
	def __init__(self, alliance, position):
		Piece.__init__(self, alliance)
		self.alliance = alliance
		self.position = position
		#print(self.sprite, self.alliance, self.position)
		
	def toString(self):
		return("P" if self.alliance == "Black" else "p")

	def movement(self, position):
		pass
