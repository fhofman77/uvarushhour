class Board():
    def __init__(self, size):
        # columns run vertical (like a y axes)
        self.col = size
        # rows run horizontal (like a x axes)
        self.row = size
        # self.exit =

        # Winning board
        # Previous Boards


class Car():
    def __init__(self, car, orientation, col, row, length):
        # in the data the last car is the car that needs to escape
        self.car = car
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length
