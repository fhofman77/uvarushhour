import random

""" 
Contains the random algorithm for solving the rushhour puzzle
"""

def random_move(board):
    # choose a random car to move
    car = random.choice(board.vehicles)
    number = random.randrange(1, board.size-1)
    if random.random() < 0.5:
        number = number 
    else:
        number = -number
    if board.move_car(car, number):
        return [car.car, number]