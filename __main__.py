import pdb
import sys
import pygame
from board.chessBoard import Board
import board.move as mv
from pieces.nullPiece import NullPiece


whos_turn = 'White'

pygame.init()

display_width = 800
display_height = 800
currently_selected_square = None

'''
#the MAIN class which holds all the pieces
gameTiles = {}
is a 64 int dictionary which holds the instance of the class Tile

chessBoard.gameTiles[int 0-63]  <-- selects the tile

'''
chessBoard = Board()
chessBoard.createBoard()

#creates a canvas called gameDisplay
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()
crashed = False





########################################################################
########################################################################

#list of tiles, w, h, etc. to be blited ([color, [x,y,w,h]])
allTiles = []
#64 int list with piece:   [img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile]
allPieces = []


def squares(x, y, w, h, color):
	pygame.draw.rect(gameDisplay, color, [x,y,w,h])
	allTiles.append([color, [x,y,w,h]])

#draws the board without pieces
def drawChessPieces():
	xpos = 0
	ypos = 0
	#color = 0
	width = display_width/8
	height = display_height/8
	square_color = {'white': (143,155,175), 'black': ((66,0,0))}
	number = 0

	for _ in range(8):
		for _ in range(8):
			#draw the square
			squares(xpos, ypos, width, height, square_color[chessBoard.gameTiles[number].tile_color])
			chessBoard.gameTiles[number].xpos = xpos
			chessBoard.gameTiles[number].ypos = ypos
			#if square not empty, add image of piece to allPieces list
			if not chessBoard.gameTiles[number].pieceOnTile.toString() == '-':
				img = pygame.image.load("./ChessArt/"+chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper()+chessBoard.gameTiles[number].pieceOnTile.toString().upper()+".png")
				img = pygame.transform.scale(img, (int(display_width/8),int(display_height/8)))
				allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
			xpos += display_width/8
			number += 1
		xpos = 0
		ypos += display_height/8


	'''
	for _ in range(8):
		for _ in range(8):
			if color % 2 == 0:
				#draw the square
				squares(xpos, ypos, width, height, white)
				#if square not empty, add image of piece to allPieces list
				if not chessBoard.gameTiles[number].pieceOnTile.toString() == '-':
					img = pygame.image.load("./ChessArt/"+chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper()+chessBoard.gameTiles[number].pieceOnTile.toString().upper()+".png")
					img = pygame.transform.scale(img, (int(display_width/8),int(display_height/8)))
					allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])

				xpos += display_width/8

			else:
				squares(xpos, ypos, width, height, black)
				if not chessBoard.gameTiles[number].pieceOnTile.toString() == '-':
					img = pygame.image.load("./ChessArt/"+chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper()+chessBoard.gameTiles[number].pieceOnTile.toString().upper()+".png")
					img = pygame.transform.scale(img, (int(display_width/8),int(display_height/8)))
					allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
				xpos += display_width/8

			color += 1
			number += 1

		color += 1
		xpos = 0
		ypos += display_height/8
		'''




########################################################################
########################################################################
drawChessPieces()

while not crashed:

	#evaluates what happens during each event (x # of frames), (where mouse is, if event is quit, etc.)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			#integer from 0-63
			clicked_square = mv.which_square(mouse_x, mouse_y, display_width, display_height)

			#pdb.set_trace()
			#print(chessBoard.gameTiles[clicked_square].alliance)

			
			#if piece is selected, unselect
			if currently_selected_square == clicked_square:
				allPieces = [x for x in allPieces if len(x) != 2]
				currently_selected_square = None


			#if no piece is selected, select the square (if legal) and display moves
			elif chessBoard.gameTiles[clicked_square].pieceOnTile.alliance == whos_turn:
				allPieces = [x for x in allPieces if len(x) != 2]

				#highlight selected square
				img = pygame.image.load("./ChessArt/red_square.png")
				img = pygame.transform.scale(img, (int(display_width/8),int(display_height/8)))
				allPieces.append([img, [chessBoard.gameTiles[clicked_square].xpos, chessBoard.gameTiles[clicked_square].ypos]])

				#calculate legal moves
				mv.return_list_of_legal_moves(chessBoard.gameTiles[clicked_square])

				#NEED FUNCTION TO BLOCK SQUARES!!
				#legal_moves = blocked_squares(chessBoard)
				legal_moves = chessBoard.gameTiles[clicked_square].pieceOnTile.movement(chessBoard.gameTiles[clicked_square].tileCoordinate)

				#display legal moves
				if legal_moves is not None:
					img = pygame.image.load("./ChessArt/red_dot.png")
					img = pygame.transform.scale(img, (int(display_width/8),int(display_height/8)))
					for legal_move in legal_moves:
						#print([img, [chessBoard.gameTiles[legal_move].xpos, chessBoard.gameTiles[legal_move].ypos]])
						allPieces.append([img, [chessBoard.gameTiles[legal_move].xpos, chessBoard.gameTiles[legal_move].ypos]])
				currently_selected_square = clicked_square



			#if square is already select, and you select another square
			elif currently_selected_square is not None:
				if legal_moves is not None and clicked_square in legal_moves:
					chessBoard.gameTiles[clicked_square].pieceOnTile = chessBoard.gameTiles[currently_selected_square].pieceOnTile
					chessBoard.gameTiles[currently_selected_square].pieceOnTile = NullPiece
					allPieces = mv.rebuild_sprites(chessBoard.gameTiles, display_width, display_height)

					legal_moves = None
					currently_selected_square = None
				pass





			else:
				pass
				#check if legal square
				#if legal, move piece,
					#get square # and piece from square
					#find legal moves
					#add red dots to allPieces
				#if own square, select square
				#else do nothing


			#select_square()  - if you can, check if correct color check if in check			
			#blit square
			#if currently_selected_square = None:
			#currently_selected_square = selected square
			#draw red square
			#if currently selected is same as current square, selected sqare = none
			#else: evaluate all legal moves, draw circles
			#pygame.draw.square(parameters)
			#pygame.display.update()
			#screen.blit(param) updates only that part of the screen
		#print(event)
	#draws the pieces. img[0] is specific surface, img[1] is position

	#gameDisplay.fill([255,255,255])




	for img in allTiles:
		pygame.draw.rect(gameDisplay, img[0], img[1])

#64 int list with piece:   [img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile]
	for img in allPieces:
		gameDisplay.blit(img[0], img[1])



	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()