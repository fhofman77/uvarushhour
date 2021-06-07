from code.visualisation.visualise import print_board
from code.classes.objects import Board, get_board_size, moves

inputdata = 'data/gameboards/Rushhour6x6_3.csv'
# Load all the vehicles

board = Board(inputdata)
print(board.get_board_size)


print(board.vehicles[5].car)

board.vehicles[0].valid_move(-2, board)
board.vehicles[5].valid_move(-2, board)
