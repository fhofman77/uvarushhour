import csv
import re
from code.visualisation.visualise import print_board


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

    for car in vehicles:
        if car.orientation == 'H':
            car.coordinate_row.append(car.row)
            for i in range(int(car.length)):
                y = car.col
                y += i
                car.coordinate_col.append(y)
        else:
            car.coordinate_col.append(car.col)
            for i in range(int(car.length)):
                x = car.row
                x += i
                car.coordinate_row.append(x)

    return vehicles


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
        self.vehicles = initialize_cars(inputdata)

    def size(self):
        return self.size

    def winning_board(self):
        """Add Desired End Board"""
        # Last car of the csv-input is completely on the right side means it's WON
        pass

    def print_board(self):
        return print_board(self.vehicles, self.size)

    def current_board(self):
        """Add current board (after moves made)"""
        pass

    def won_game(self):
        """If end_board == current_board return true"""
        pass

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
        self.coordinate_row = []
        self.coordinate_col = []

    def move(self, distance, board):
        valid_move(distance, board)

        # If the car is moved, append to moves dictionairy
        if distance != 0:
            moves[self.car] = distance

        """Still need to UPDATE BOARD && CHECK valid_move"""
        new_position = self.col + distance

        # Move the car
        if self.orientation == 'H':
            self.col = new_position
            self.coordinate_col = [i + distance for i in self.coordinate_col]
        if self.orientation == 'V':
            self.row = new_position
            self.coordinate_row = [i + distance for i in self.coordinate_col]

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
