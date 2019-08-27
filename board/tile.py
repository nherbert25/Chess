class Tile:

	pieceOnTile = None
	tile_color = None
	tileCoordinate = None
	piece_selected = False
	legal_move = False
	
	def __init__(self,coordinate,color,piece,selected,legal):
		self.tileCoordinate = coordinate
		self.tile_color = color
		self.pieceOnTile = piece
		self.piece_selected = selected
		self.legal_move = legal