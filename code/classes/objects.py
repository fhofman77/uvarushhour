import csv
import re
from code.visualisation.visualise import print_board
from code.algorithms.random import random_move


def initialize_cars(csv_input):
    vehicles = []
    with open(csv_input, newline='') as gamefile:
        rows = csv.reader(gamefile, delimiter=',')
        next(rows)
        for row in rows:
            vehicle = Car(row[0], row[1], row[2], row[3], row[4])
            vehicles.append(vehicle)

    # Printen misschien beter in een andere functie
    # Dit werkt nu niet voor boards met een andere size dan 6, ook klopt de logica niet
    occupied_row_col = []
    for car in vehicles:
        if car.orientation == 'H':
            for i in range(int(car.length)):
                y = car.col
                y += i
                occupied_row_col.append([car, car.row, y])
        else:
            for i in range(int(car.length)):
                x = car.row
                x += i
                occupied_row_col.append([car, x, car.col])

    return vehicles, occupied_row_col


moves = {
    'car': 'move'
}


def get_board_size(inputdata):
    """Finds the value between 'Rushhour' and 'x' and returns it as an int"""
    board_size = re.search('Rushhour(.*)x', inputdata)
    board_size = int((board_size.group(1)))
    return board_size


class Board():
    def __init__(self, inputdata):
        self.size = get_board_size(inputdata)
        # Columns run vertical (like a y axes)
        self.col = get_board_size(inputdata)
        # Rows run horizontal (like a x axes)
        self.row = get_board_size(inputdata)
        self.vehicles, self.occupied_row_col = initialize_cars(
            inputdata)

    def size_function(self):
        return int(self.size)

    def winning_board(self, board):
        """Add Desired End Board"""
        if vehicles.col[-1] == board_size and vehicles.row[-1] == int(board_size/2):
            return True
        return False

        # Last car of the csv-input is completely on the right side means it's WON
        pass

    def move_car(self, car, distance):
        # If the car is moved, append to moves dictionairy
        if distance != 0:
            moves[car.car] = distance

        """Still need to UPDATE BOARD && CHECK valid_move"""
        board = Board

        if self.valid_move(car, distance):
            new_position = car.col + distance
        else:
            return

        # Move the car
        if car.orientation == 'H':
            car.col = new_position
            # car.coordinate_col = [i + distance for i in car.coordinate_col]
            for i in car.coordinate_col:
                new = i + distance
                car.coordinate_col[i] = new
            if car.car == 'X':
                print(f'test {car.coordinate_col}')

            print(f'{car.car} H car is moved')
        if car.orientation == 'V':
            car.row = new_position
            car.coordinate_row = [i + distance for i in car.coordinate_col]
            print(f'{car.car} V car is moved')

    def print_board(self):
        return print_board(self.vehicles, self.size)

    def current_board(self):
        """Add current board (after moves made)"""
        pass

    def won_game(self, board):
        """If end_board == current_board return true"""
        pass

    def past_board(self):
        """if the current board == a past board after doing moves, it cant be the fastest so keep track of the past boards"""
        pass

    def valid_move(self, car, distance):
        if car.orientation == 'H':
            if distance < 0:
                start = car.col
                end = car.col + distance
                if end < 1:
                    return False
            else:
                start = car.col
                end = car.col + distance + (car.length - 1)
                x = 6
                if end > x:
                    return False

            for car in self.vehicles:
                if car.row == car.row or car.row in car.coordinate_row:
                    if car is not car:
                        for value in car.coordinate_col:
                            # If we move to the left 
                            if distance < 0:
                                # If the value of the car is in between the start and endpoint
                                if end <= int(value) <= start:
                                    return False
                                else:
                                    return True
                            # If we move to the right
                            else:
                                # If the value of the car is in between the start and endpoint
                                if start <= value <= end:
                                    return False
                                else:
                                    return True

        # If the car is vertical
        else:
            # Move up
            if distance < 0:
                start = car.row + car.length - 1
                end = car.row + distance
                print(f'start: {start} End: {end}')
                if end < 1:
                    print("Out of topside self")
                    return False

            # Move down
            else:
                start = car.row
                end = car.row + distance + (car.length - 1)
                print(f'start: {start} End: {end}')
                if end > self.size:
                    print("Out of bottom")
                    return False

            # For each car on the self
            for car in self.vehicles:

                # If the car is in the same
                if car.col in car.coordinate_col or car.col == car.col:
                    # En het is niet deze auto
                    if car is not car:
                        print("not car")
                        for value in car.coordinate_row:
                            # If we move to the top
                            if distance < 0:
                                # If the value of the car is in between the start and endpoint
                                if start <= value <= end:
                                    print(f'{car.car} in the way')
                                    return False
                                else:
                                    print('Moved top Good move')
                                    return True
                            # If we move to the bottom
                            else:
                                # If the value of the car is in between the start and endpoint
                                if start <= value <= end:
                                    print(f'Moved bottom but {car.car} in the way')
                                    return False
                                else:
                                    print('Moved bottom good move')
                                    return True


class Car():
    def __init__(self, car, orientation, col, row, length):
        # In the data the last car is the car that needs to escape
        self.car = car
        self.orientation = orientation
        self.col = int(col)
        self.row = int(row)
        self.length = int(length)
        self.moves = []
        self.coordinate_row = []
        self.coordinate_col = []
