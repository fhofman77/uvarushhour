from code.classes.objects import Board
from code.classes.algorithms import random

inputdata = 'data/gameboards/Rushhour6x6_3.csv'
# Load all the vehicles

board = Board(inputdata)

# Deze print werkt

print(board.occupied_row_col)

