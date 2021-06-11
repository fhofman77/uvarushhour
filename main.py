from code.classes.objects import Board, moves
from code.algorithms.random import random_move
from collections import OrderedDict

inputdata = 'data/gameboards/Rushhour6x6_2.csv'
# Load all the vehicles

board = Board(inputdata)

board.get_possible_moves()
board.print()
