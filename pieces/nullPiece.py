from pieces.piece import Piece

class NullPiece(Piece):

	alliance = None
	position = None
	name = 'empty'
	
	def __init__(self):
		pass
		
	def toString(self):
		return "-"