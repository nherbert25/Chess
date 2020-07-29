import pygame

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



#board_state is boolean list of 64 squares, 0 for black piece
def return_list_of_legal_moves(Tile):
    Piece = Tile.pieceOnTile
    position = Tile.tileCoordinate
    alliance = Piece.alliance
    board_state = None
    potential_legal_moves = [Piece.movement(position)]




    #print(Piece, position, alliance, board_state)
    #Tile.tileCoordinate = 14
    #print(potential_legal_moves)




#detects collisions, removes illegal squares
#takes in piece clicked, square clicked, and tuple of square and alliance of all other tiles (3, w)  returns legal moves

#rebuild sprites on tiles
def rebuild_sprites(board, display_width, display_height):
    allPieces = []
    for key,value in (board.items()):
        #print(key, value)
        #return allPieces datatype

        if value.pieceOnTile.sprite is not None:
            print(value.pieceOnTile) #NullPiece

            img = pygame.image.load(value.pieceOnTile.sprite)
            img = pygame.transform.scale(img, (int(display_width/8),int(display_height/8)))
            allPieces.append([img, [value.xpos, value.ypos], value.pieceOnTile])
    
    return(allPieces)
        #if board[key]
        #allPieces.append[clicked_square] = [img, [chessBoard.gameTiles[clicked_square].xpos, chessBoard.gameTiles[clicked_square].ypos], chessBoard.gameTiles[clicked_square].pieceOnTile]

