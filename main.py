
from code.algorithms.random import random_move
from code.visualisation.visualise import print_board
from code.classes.objects import Board, moves, Car

inputdata = 'data/gameboards/Rushhour6x6_3.csv'
# Load all the vehicles

board = Board(inputdata)

# Deze print werkt

print(board.occupied_row_col)
print_board(board.occupied_row_col, board.size)

for item in board.occupied_row_col:
    if item[0] == board.vehicles[1].car:
        print(item)


board.valid_vertical_move(board.vehicles[1], 3, 5)

print(moves)
