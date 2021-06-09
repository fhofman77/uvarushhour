import csv
import re
from code.visualisation.visualise import print_board
import numpy as np


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
                occupied_row_col.append([car.car, car.row, y])
        else:
            for i in range(int(car.length)):
                x = car.row
                x += i
                occupied_row_col.append([car.car, x, car.col])

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

    def size(self):
        return self.size

    def move_car(self, car, distance):
        """Change car.car to car"""
        for item in self.occupied_row_col:
            if item[0] == car.car and car.orientation == "H":
                if self.valid_horizontal_move(car, item[2], item[2]+distance) == True:
                    item[2] = item[2] + distance
                    moves[car.car] = distance

            if item[0] == car.car and car.orientation == "V":
                if self.valid_vertical_move(car, item[1], item[1]+distance) == True:
                    item[1] = item[1] + distance
                    moves[car.car] = distance

    def valid_vertical_move(self, car, startpoint, endpoint):
        """Change to car instead of car.car"""
        for item in self.occupied_row_col:
            # If a car from a board is in the same collumn
            if item[2] == car.col:
                # If it is a different car and the cars collide, return False
                if item[0] is not car.car and ((startpoint <= item[1] <= endpoint) or (endpoint <= item[1] <= startpoint)):
                    return False
        else:
            return True

    def valid_horizontal_move(self, car, startpoint, endpoint):
        """Change to car instead of car.car"""
        for item in self.occupied_row_col:
            # If the car from the board is in the same row
            if item[1] == car.row:
                # If the car is not the car, and the vehicles collide return false
                if item[0] is not car.car and ((startpoint <= item[2] <= endpoint) or (endpoint <= item[2] <= startpoint)):
                    return False
        else:
            return True

    def print_board(self):
        pass

    def current_board(self):
        """Add current board (after moves made)"""
        return self.occupied_row_col
        pass

    def won_game(self):
        """If end_board == current_board return true"""
        win_loc_x = np.ceil(self.size(self) / 2)
        win_loc_y = self.size(self)

        escape_car = self[-1]
        if escape_car[0].car == 'X':
            if escape_car[-2] == win_loc_x and escape_car[-1] == win_loc_y:
                return True
            else:
                return False
        else:
            return False

    def past_board(self):
        """if the current board == a past board after doing moves, it cant be the fastest so keep track of the past boards"""
        pass


class Car():
    def __init__(self, car, orientation, col, row, length):
        # In the data the last car is the car that needs to escape
        self.car = car
        self.orientation = orientation
        self.col = int(col)
        self.row = int(row)
        self.length = int(length)
        self.moves = []

    def valid_move(self, distance, board):
        if self.orientation == 'H':
            if distance < 0:
                start = self.col
                end = self.col + distance
                if end < 1:
                    return False
            else:
                start = self.col
                end = self.col + distance + (self.length - 1)
                if end > board.size:
                    return False

            for car in board.vehicles:
                if car.row == self.row or self.row in car.coordinate_row:
                    if car is not self:
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
                start = self.row + self.length - 1
                end = self.row + distance
                print(f'start: {start} End: {end}')
                if end < 1:
                    print("Out of topside Board")
                    return False

            # Move down
            else:
                start = self.row
                end = self.row + distance + (self.length - 1)
                print(f'start: {start} End: {end}')
                if end > board.size:
                    print("Out of bottom")
                    return False

            # For each car on the board
            for car in board.vehicles:

                # If the car is in the same
                if self.col in car.coordinate_col or self.col == car.col:
                    print(car.car)
                    # En het is niet deze auto
                    if car is not self:
                        print("not self")
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
                                    print(
                                        f'Moved bottom but {car.car} in the way')
                                    return False
                                else:
                                    print('Moved bottom good move')
                                    return True
