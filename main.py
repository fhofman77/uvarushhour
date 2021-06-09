from code.classes.objects import Board, moves
from code.visualisation.visualise import print_board

inputdata = 'data/gameboards/Rushhour6x6_3.csv'
# Load all the vehicles

board = Board(inputdata)

# Deze print werkt


for item in board.occupied_row_col:
    if item[0] == board.vehicles[1].car:
        print(item)


board.valid_vertical_move(board.vehicles[1], 3, 5)
print_board(board.occupied_row_col, board.size)

print(moves)
