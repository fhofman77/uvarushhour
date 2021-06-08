from code.classes.objects import Board, Car
from code.algorithms.random import random_move

inputdata = 'data/gameboards/Rushhour6x6_3.csv'
# Load all the vehicles

board = Board(inputdata)

# Deze print werkt

print(board.occupied_row_col)
print(board.vehicles[-1].col)
while board.occupied_row_col[-1] != '6' :
   random_move(board)
else:
    print('won game')

