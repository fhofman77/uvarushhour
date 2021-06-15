import random

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