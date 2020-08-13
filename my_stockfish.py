#https://pypi.org/project/stockfish/
from stockfish import Stockfish


stockfish = Stockfish('Q:/stockfish-11-win/Windows/stockfish_20011801_x64.exe')

playing_computer = True




#stockfish = Stockfish(parameters={"Threads": 2, "Minimum Thinking Time": 30})
#stockfish.set_position(['e2e4', 'e7e6', 'd2d4', 'd8h4','b1c3', 'f8b4','f1d3','b8c6','g1f3','h4g4','e1g1','g4h5','c3b5','b4a5','c1d2','a5b6', 'a2a4', 'h7h6','a4a5','g7g6','a5a6','g6g5','a6b7','g5g4','b7a8n', 'g4g3','d1e2','f7f6'])

#print(stockfish.get_board_visual())
#print(stockfish.get_best_move())

#print(stockfish.get_best_move_time(1000))

#print(stockfish.get_board_visual())