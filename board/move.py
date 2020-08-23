import pygame
from pieces.nullPiece import NullPiece
import pdb

#takes in x,y of where you click, returns the square which you clicked as an integer 0-63
def which_square(mouse_x, mouse_y, display_width, display_height):
    square = 0
    if mouse_x < display_width/8:
        pass
    elif mouse_x < 2*display_width/8:
        square +=1
    elif mouse_x < 3*display_width/8:
        square +=2
    elif mouse_x < 4*display_width/8:
        square +=3
    elif mouse_x < 5*display_width/8:
        square +=4
    elif mouse_x < 6*display_width/8:
        square +=5
    elif mouse_x < 7*display_width/8:
        square +=6
    elif mouse_x < 8*display_width/8:
        square +=7
    if mouse_y < display_height/8:
        pass
    elif mouse_y < 2*display_height/8:
        square +=8
    elif mouse_y < 3*display_height/8:
        square +=16
    elif mouse_y < 4*display_height/8:
        square +=24
    elif mouse_y < 5*display_height/8:
        square +=32
    elif mouse_y < 6*display_height/8:
        square +=40
    elif mouse_y < 7*display_height/8:
        square +=48
    elif mouse_y < 8*display_height/8:
        square +=56
    return(square)



#rebuild sprites on tiles
def rebuild_sprites(board, display_width, display_height):
    allPieces = []
    for key,value in (board.items()):
        #print(key, value)
        #return allPieces datatype

        if value.pieceOnTile.sprite is not None:
            #print(value.pieceOnTile) #NullPiece

            img = pygame.image.load(value.pieceOnTile.sprite)
            img = pygame.transform.scale(img, (int(display_width/8),int(display_height/8)))
            allPieces.append([img, [value.xpos, value.ypos], value.pieceOnTile])

    return(allPieces)






def move_piece(currently_selected_square, clicked_square, chessBoard, display_width, display_height, whos_turn):

    #check promotion
    if (clicked_square <= 7 or clicked_square >= 56) and chessBoard.gameTiles[currently_selected_square].pieceOnTile.can_promote == True:
        chessBoard.gameTiles[currently_selected_square].pieceOnTile = chessBoard.promote(chessBoard.gameTiles[currently_selected_square])
    
    #if castling, move the rook
    if chessBoard.gameTiles[currently_selected_square].pieceOnTile.name  == 'king' and clicked_square - currently_selected_square == 2:
        chessBoard.gameTiles[currently_selected_square+1].pieceOnTile = chessBoard.gameTiles[currently_selected_square+3].pieceOnTile
        chessBoard.gameTiles[currently_selected_square+1].pieceOnTile.has_moved = True
        chessBoard.gameTiles[currently_selected_square+3].pieceOnTile = NullPiece()
    
    if chessBoard.gameTiles[currently_selected_square].pieceOnTile.name  == 'king' and clicked_square - currently_selected_square == -2:
        chessBoard.gameTiles[currently_selected_square-1].pieceOnTile = chessBoard.gameTiles[currently_selected_square-4].pieceOnTile
        chessBoard.gameTiles[currently_selected_square-1].pieceOnTile.has_moved = True
        chessBoard.gameTiles[currently_selected_square-4].pieceOnTile = NullPiece()

    #move piece
    chessBoard.gameTiles[clicked_square].pieceOnTile = chessBoard.gameTiles[currently_selected_square].pieceOnTile
    chessBoard.gameTiles[clicked_square].pieceOnTile.has_moved = True
    chessBoard.gameTiles[currently_selected_square].pieceOnTile = NullPiece()
    allPieces = rebuild_sprites(chessBoard.gameTiles, display_width, display_height)

    #reset global variables
    chessBoard.record_move(currently_selected_square, clicked_square)
    legal_moves = None
    currently_selected_square = None
    if whos_turn == 'White':
        whos_turn = 'Black'
    else:
        whos_turn = 'White'
    return(allPieces, whos_turn)
