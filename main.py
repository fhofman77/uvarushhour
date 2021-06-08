from code.classes.objects import Board
from code.classes.algorithms import random

inputdata = 'data/gameboards/Rushhour6x6_3.csv'
# Load all the vehicles

board = Board(inputdata)

# Deze print werkt
board.print_board()

# Dit zijn de goede waardes
print(f'{board.vehicles[1].car}: ROW {board.vehicles[1].coordinate_row}')
print(f'{board.vehicles[1].car}: COL {board.vehicles[1].coordinate_col}')
print(f'{board.vehicles[5].car}: ROW {board.vehicles[5].coordinate_row}')
print(f'{board.vehicles[5].car}: COL {board.vehicles[5].coordinate_col}')

# 1 beweging
board.vehicles[1].move(1, board)
# Deze print werkt niet meer
# board.print_board()
