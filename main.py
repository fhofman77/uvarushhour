from code.classes.objects import Board, moves
from code.algorithms.random import random_move
from collections import OrderedDict

inputdata = 'data/gameboards/Rushhour6x6_2.csv'
# Load all the vehicles

board = Board(inputdata)


# while not board.won_game():
#     random_move(board)
#     board.print()
 

print(moves)


