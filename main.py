
from code.algorithms.random import random_move
from code.algorithms.breath_first import breath_algorithm
from code.visualisation.visualise import print_board
from code.classes.objects import Board, moves, Car

inputdata = 'data/gameboards/Rushhour6x6_2.csv'
# Load all the vehicles

board = Board(inputdata)



# while not board.won_game():
#     random_move(board)
#     board.print()
 

# print(moves)

breath_algorithm(board)

# board.move_car(board.vehicles[0], -1)
# board.print()
# board.move_car(board.vehicles[0], -1)
# board.print()
# board.move_car(board.vehicles[-1], -1)
# board.print()
# board.move_car(board.vehicles[-1], -1)
# board.print()

