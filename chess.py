import sys
import pygame
import board.move as mv
import my_stockfish as stockfish
from board.chessBoard import Board
from pieces.nullPiece import NullPiece

pygame.init()

display_width = 800
display_height = 800
whos_turn = 'White'
currently_selected_square = None

'''
#the MAIN class which holds all the pieces
chessBoard.gameTiles = {}
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


#allows for text to overlay the screen
black = (0,0,0)
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()

def checkmate():
	chessBoard.checkmate = True
	message_display('Checkmate!')

	while chessBoard.checkmate:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		pygame.display.update()
		clock.tick(15)

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



########################################################################
########################################################################
#main loop
drawChessPieces()
chessBoard.legal_moves = chessBoard.hash_legal_moves(whos_turn)

while not crashed:

	#evaluates what happens during each event (x # of frames), (where mouse is, if event is quit, etc.)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
			print(chessBoard.game_position)
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			clicked_square = mv.which_square(mouse_x, mouse_y, display_width, display_height)

			
			#if square is already selected, unselect
			if currently_selected_square == clicked_square:
				allPieces = [x for x in allPieces if len(x) != 2]
				currently_selected_square = None


			#if square selected has a piece of your alliance on it, select the square and display moves
			elif chessBoard.gameTiles[clicked_square].pieceOnTile.alliance == whos_turn:
				allPieces = [x for x in allPieces if len(x) != 2]

				#highlight selected square
				img = pygame.image.load("./ChessArt/red_square.png")
				img = pygame.transform.scale(img, (int(display_width/8),int(display_height/8)))
				allPieces.append([img, [chessBoard.gameTiles[clicked_square].xpos, chessBoard.gameTiles[clicked_square].ypos]])

				#calculate legal moves
				#legal_moves = chessBoard.return_list_of_legal_moves(clicked_square)
				legal_moves = chessBoard.legal_moves.get(clicked_square)

				#display legal moves
				if legal_moves is not None:
					img = pygame.image.load("./ChessArt/red_dot.png")
					img = pygame.transform.scale(img, (int(display_width/30),int(display_height/30)))
					for legal_move in legal_moves:
						allPieces.append([img, [chessBoard.gameTiles[legal_move].xpos+display_width/16-img.get_width()//2, chessBoard.gameTiles[legal_move].ypos+display_height/16-img.get_width()//2]])
				currently_selected_square = clicked_square





			#if a piece is already select and you select a legal move, move the piece and change turns
			elif currently_selected_square is not None:
				if legal_moves is not None and clicked_square in legal_moves:

					#move piece
					allPieces, whos_turn = mv.move_piece(currently_selected_square, clicked_square, chessBoard, display_width, display_height, whos_turn)
					
					if stockfish.playing_computer == True:
						stockfish.stockfish.set_position(chessBoard.game_position)
						currently_selected_square, clicked_square = chessBoard.invert_recorded_move(stockfish.stockfish.get_best_move())
						allPieces, whos_turn = mv.move_piece(currently_selected_square, clicked_square, chessBoard, display_width, display_height, whos_turn)

					currently_selected_square = None



			else:
				pass
	#end of user input logic



	#draw all tiles
	for img in allTiles:
		pygame.draw.rect(gameDisplay, img[0], img[1])

	#64 int list with piece:   [img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile]
	for img in allPieces:
		gameDisplay.blit(img[0], img[1])

	pygame.display.update()
	chessBoard.legal_moves = chessBoard.hash_legal_moves(whos_turn)

	#if checkmate, end game
	if not chessBoard.legal_moves:
		checkmate()

	clock.tick(60)

pygame.quit()
quit()