import csv
import re
from code.visualisation.visualise import print_board


def initialize_cars(csv_input):
    """
    Loads the board and car objects from the csv file
    """
    # read and store vehicle information from file in correct order
    vehicles = []
    with open(csv_input, newline='') as gamefile:
        rows = csv.reader(gamefile, delimiter=',')
        next(rows)
        for row in rows:
            vehicle = Car(row[0], row[1], row[2], row[3], row[4])
            vehicles.append(vehicle)

    # Create the occupied rows and columns matrix of the board based on orientation and length of the cars
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


def get_board_size(inputdata):
    """
    Finds the value between 'Rushhour' and 'x' and returns it as an int
    """
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

    def move_car(self, car, distance):
        """
        Moves a car in the occupied row/col matrix if the move is legal
        """
        move_made = 0
        # First check if the move is valid, if it is not return false
        for item in self.occupied_row_col:
            if item[0] == car.car and car.orientation == "H":
                if self.valid_horizontal_move(car, item[2], item[2]+distance) == False:
                    return False
            if item[0] == car.car and car.orientation == "V":

                if self.valid_vertical_move(car, item[1], item[1]+distance) == False:
                    return False

        # Execute the move based on the give distance and board
        for item in self.occupied_row_col:
            if item[0] == car.car and car.orientation == "H":
                item[2] = item[2] + distance
                move_made += 1

            if item[0] == car.car and car.orientation == "V":
                item[1] = item[1] + distance
                move_made += 1

        # Check for moving a car, as we move multiple spaces
        if move_made > 0:
            return True
        else:
            return False

    def print(self):
        """
        Prints a visual representation of the board
        """
        return print_board(self.occupied_row_col, self.size)

    def valid_vertical_move(self, car, startpoint, endpoint):
        """
        Checks if a vertical move is possible
        """
        if endpoint <= 0 or endpoint > self.size:
            return False
        for item in self.occupied_row_col:
            # If a car from a board is in the same collumn
            if item[2] == car.col:
                # If it is a different car and the vehicles collide, return false
                if item[0] is not car.car and ((startpoint <= item[1] <= endpoint) or (endpoint <= item[1] <= startpoint)):
                    return False
        else:
            return True

    def valid_horizontal_move(self, car, startpoint, endpoint):
        """
        Checks if a horizontal move is possible
        """
        if endpoint <= 0 or endpoint > self.size:
            return False

        # Change to car instead of car.car
        for item in self.occupied_row_col:
            # If the car from the board is in the same row
            if item[1] == car.row:
                # If the car is not the car, and the vehicles collide return false
                if item[0] is not car.car and ((startpoint <= item[2] <= endpoint) or (endpoint <= item[2] <= startpoint)):
                    return False

        return True

    def won_game(self):
        """
        Returns True if the game is won
        """
        escape_car = self.occupied_row_col[-1]
        if escape_car[2] == 6:
            return True
        else:
            return False


class Car():
    """
    The car object is mostly used to return its orientation and the car name
    """

    def __init__(self, car, orientation, col, row, length):
        self.car = car
        self.orientation = orientation
        self.col = int(col)
        self.row = int(row)
        self.length = int(length)
