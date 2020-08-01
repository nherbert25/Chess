import copy

from board.tile import Tile
from pieces.nullPiece import NullPiece
from pieces import bishop
from pieces import king
from pieces import knight
from pieces import rook
from pieces import queen
from pieces import pawn

class Board:

	gameTiles = {}
	
	def __init__(self):
		pass
		
	def createBoard(self):
		for tile in range(64):
			self.gameTiles[tile] = Tile(tile, 'white', NullPiece(), False, False)        

		self.gameTiles[0] = Tile(0, 'white', rook.Rook("Black", 0), False, False)
		self.gameTiles[1] = Tile(1, 'black', knight.Knight("Black", 1), False, False)
		self.gameTiles[2] = Tile(2, 'white', bishop.Bishop("Black", 2), False, False)
		self.gameTiles[3] = Tile(3, 'black', queen.Queen("Black", 3), False, False)
		self.gameTiles[4] = Tile(4, 'white', king.King("Black", 4), False, False)
		self.gameTiles[5] = Tile(5, 'black', bishop.Bishop("Black", 5), False, False)
		self.gameTiles[6] = Tile(6, 'white', knight.Knight("Black", 6), False, False)
		self.gameTiles[7] = Tile(7, 'black', rook.Rook("Black", 7), False, False)
		self.gameTiles[8] = Tile(8, 'black', pawn.Pawn("Black", 8), False, False)
		self.gameTiles[9] = Tile(9, 'white', pawn.Pawn("Black", 9), False, False)
		self.gameTiles[10] = Tile(10, 'black', pawn.Pawn("Black", 10), False, False)
		self.gameTiles[11] = Tile(11, 'white', pawn.Pawn("Black", 11), False, False)
		self.gameTiles[12] = Tile(12, 'black', pawn.Pawn("Black", 12), False, False)
		self.gameTiles[13] = Tile(13, 'white', pawn.Pawn("Black", 13), False, False)
		self.gameTiles[14] = Tile(14, 'black', pawn.Pawn("Black", 14), False, False)
		self.gameTiles[15] = Tile(15, 'white', pawn.Pawn("Black", 15), False, False)

		count1 = 0
		count2 = 0
		color = ['white','black']
		for tile in range(16,48):
			for _ in range(8):
				self.gameTiles[tile] = Tile(tile, color[count1%2], NullPiece(), False, False)
			count1+=1
			count2+=1
			if count2%8==0:
				count1+=1
				count2=0

		self.gameTiles[48] = Tile(48, 'white', pawn.Pawn("White", 48), False, False)
		self.gameTiles[49] = Tile(49, 'black', pawn.Pawn("White", 49), False, False)
		self.gameTiles[50] = Tile(50, 'white', pawn.Pawn("White", 50), False, False)
		self.gameTiles[51] = Tile(51, 'black', pawn.Pawn("White", 51), False, False)
		self.gameTiles[52] = Tile(52, 'white', pawn.Pawn("White", 52), False, False)
		self.gameTiles[53] = Tile(53, 'black', pawn.Pawn("White", 53), False, False)
		self.gameTiles[54] = Tile(54, 'white', pawn.Pawn("White", 54), False, False)
		self.gameTiles[55] = Tile(55, 'black', pawn.Pawn("White", 55), False, False)
		self.gameTiles[56] = Tile(56, 'black', rook.Rook("White", 56), False, False)
		self.gameTiles[57] = Tile(57, 'white', knight.Knight("White", 57), False, False)
		self.gameTiles[58] = Tile(58, 'black', bishop.Bishop("White", 58), False, False)
		self.gameTiles[59] = Tile(59, 'white', queen.Queen("White", 59), False, False)
		self.gameTiles[60] = Tile(60, 'black', king.King("White", 60), False, False)
		self.gameTiles[61] = Tile(61, 'white', bishop.Bishop("White", 61), False, False)
		self.gameTiles[62] = Tile(62, 'black', knight.Knight("White", 62), False, False)
		self.gameTiles[63] = Tile(63, 'white', rook.Rook("White", 63), False, False)
			
	def printBoard(self):
		count = 0
		for tiles in range(64):
			print('|', end=self.gameTiles[tiles].pieceOnTile.toString())
			count += 1
			if count == 8:
				print('|','\r\n')
				count = 0
	
	#detects collisions, removes illegal squares
	#returns list of squares after collision
	def return_list_of_legal_moves_except_check(self, clicked_square):
		Board = self.gameTiles
		Piece = Board[clicked_square].pieceOnTile
		position = clicked_square
		alliance = Piece.alliance
		potential_legal_moves = Piece.movement(position)
		legal_moves = []


		if Piece.name == 'knight':
			for square in potential_legal_moves:
				if Board[square].pieceOnTile.alliance != alliance:
						legal_moves.append(square)
			return(legal_moves)


		if Piece.name == 'pawn':
			forward = potential_legal_moves[0]
			diagonal = potential_legal_moves[1]

			for square in forward:
				if Board[square].pieceOnTile.alliance is None:
					legal_moves.append(square)
				else:
					break
			for square in diagonal:
				if Board[square].pieceOnTile.alliance is not None and Board[square].pieceOnTile.alliance != alliance:
					legal_moves.append(square)
			return(legal_moves)


		else:
			for direction in potential_legal_moves:
				for square in direction:
					if Board[square].pieceOnTile.alliance is None:
						legal_moves.append(square)
					elif Board[square].pieceOnTile.alliance == alliance:
						break
					elif Board[square].pieceOnTile.alliance != alliance:
						legal_moves.append(square)
						break
			#print(legal_moves)

			return(legal_moves)


	
		#now check if the king would be in check

	def return_list_of_legal_moves(self, clicked_square):
		whos_turn = self.gameTiles[clicked_square].pieceOnTile.alliance
		for tile in self.gameTiles.values():
			if tile.pieceOnTile.alliance == whos_turn and tile.pieceOnTile.name == 'king':
				king_location = tile.tileCoordinate
				break

		#print(king_location)


		potential_moves = self.return_list_of_legal_moves_except_check(clicked_square)
		
		
		#alternate way instead of looping over all pieces moves is from the kings perspective!
		#write a function for the king which is the functionality of a queen + knight
		#check if the piece moves to the new square calculate all king moves,
		#if king collides with a piece which has that legal move, then king is in check


		#you can move piece to put your king in check
		#once in check, cant move any piece
		pending_moves = potential_moves
		return(pending_moves)


		#BELOW HERE IS ADDING CHECKS FUNCTION!!!!
		for potential_move in potential_moves:
			test_state = copy.deepcopy(self)
			test_board = test_state.gameTiles
			
			

			test_board[potential_move].pieceOnTile = test_board[clicked_square].pieceOnTile
			test_board[clicked_square].pieceOnTile = NullPiece
			print('pending moves: ', pending_moves)
			test_state.printBoard()
			print('Current test board state: ', 'testing move - ', test_board[potential_move].pieceOnTile.name, ' ', test_board[potential_move].tileCoordinate)
			#FIRST YOU HAVE TO IMAGINE THE PIECE HAS MOVED!, ALSO THERES A BUG, THE MOVES DO NOT COME OUT CORRECTLY EVEN WITHOUT MOVING..
			for tile in test_board.values():
				if tile.pieceOnTile.alliance is not None and tile.pieceOnTile.alliance != whos_turn:
					print(tile.tileCoordinate, tile.pieceOnTile.name, self.return_list_of_legal_moves_except_check(tile.tileCoordinate))
					if king_location in self.return_list_of_legal_moves_except_check(tile.tileCoordinate):
						if pending_moves is not None:
							pending_moves = pending_moves.remove(potential_move)
						

		print(pending_moves)
		print('-----------------------------------------------------------------------')
		return(pending_moves)
		
			#for piece on board where alliance opposite
				#find legal moves
				#if legal move puts king in check
					# remove from legal moves
					#break		