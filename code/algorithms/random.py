import random
import copy
# from code.classes import objects

""" 
Contains the algorithems for solving the rushhour puzzle
"""
def possible_move(board):
    possible = []
    
    return number



def random_move(board):
    # choose a random car to move
    car = random.choice(board.vehicles)
    
    board.move_car(board.vehicles[-1], 1)
    print(board.vehicles[-1].car ,board.vehicles[-1].coordinate_col)
    number = random.randrange(int(-board.size), int(board.size))
    board.move_car(car, number)
    return board


