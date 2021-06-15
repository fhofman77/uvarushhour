
from code.algorithms.random import random_move
from code.algorithms.breath_first import breath_algorithm
from code.visualisation.visualise import print_board, create_csv
from code.classes.objects import Board, moves, Car
import copy, time
inputdata = 'data/gameboards/Rushhour6x6_1.csv'
# Load all the vehicles

board = Board(inputdata)

moves = breath_algorithm(board)
algorithm = 'breath'
board = 'Rushhour6x6_1'


create_csv(moves, algorithm, board)

# while not board.won_game():
#     random_move(board)
#     board.print()
 

# print(moves)
# def dfs_states(board):
#     children = []
#     for car in board.vehicles:
#         for distance in range(-board.size + 1, board.size):
#             if distance != 0:
#                 current_board = copy.deepcopy(board)
#                 if current_board.move_car(car, distance):
#                     children.append(current_board)

#     return children

# def dfs_search(start_state):
#     queue = [[start_state]]
#     seen_states = set()
#     print("hello")
#     while queue:
#         path = queue.pop()
#         path[-1].print()
#         time.sleep(1)
#         if path[-1].won_game():
#             return True

#         for next_state in dfs_states(board):
#             print(next_state.print())
#             if next_state not in seen_states:
#                 seen_states.add(next_state)
#                 queue.append(path + [next_state])

# dfs_search(board)
# board.move_car(board.vehicles[0], -1)
# board.print()
# board.move_car(board.vehicles[0], -1)
# board.print()
# board.move_car(board.vehicles[-1], -1)
# board.print()
# board.move_car(board.vehicles[-1], -1)
# board.print()

