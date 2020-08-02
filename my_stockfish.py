#https://pypi.org/project/stockfish/


#import stockfish
#from stockfish import Stockfish

print('--------------------------------------------------------------------')
from stockfish import Stockfish

stockfish = Stockfish(parameters={"Threads": 2, "Minimum Thinking Time": 30})
stockfish.set_position(['e2e4', 'e7e6'])

print(stockfish.get_best_move())

