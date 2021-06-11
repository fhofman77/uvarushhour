import random
import copy
# from code.classes import objects

""" 
Contains the algorithems for solving the rushhour puzzle
"""


def random_move(board):
    # choose a random car to move
    car = random.choice(board.vehicles)
    number = random.randrange(1, board.size-1)
    if random.random() < 0.5:
        number = number
    else:
        number = -number
    board.move_car(car, number)

# try:
    #     board.move_car(board.vehicles[-1], 1)
    # except:


def get_neighbours(board):
    neighbour_states = []
    while True:
        pass

