from code.classes.objects import Board, moves

inputdata = 'data/gameboards/Rushhour6x6_3.csv'
# Load all the vehicles

board = Board(inputdata)

# Deze print werkt

print(board.occupied_row_col)

board.move_car(board.vehicles[0], 3)
board.move_car(board.vehicles[1], 3)
print(moves)