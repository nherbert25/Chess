from pieces.piece import Piece

class NullPiece(Piece):

	alliance = None
	position = None
	
	def __init__(self):
		pass
		
	def toString(self):
		return "-"