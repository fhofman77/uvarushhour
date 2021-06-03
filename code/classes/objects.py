moves = {
    'car': 'move'
}


class Board():
    def __init__(self, size):
        # columns run vertical (like a y axes)
        self.col = size
        # rows run horizontal (like a x axes)
        self.row = size

        """Add Desired End Board"""
        """Add current board"""


class Car():
    def __init__(self, car, orientation, col, row, length):
        # in the data the last car is the car that needs to escape
        self.car = car
        self.orientation = orientation
        self.col = int(col)
        self.row = int(row)
        self.length = int(length)
        self.moves = []

    def move(self, distance):
        # if the car is moved, append to moves
        if distance != 0:
            moves[self.car] = distance

        """Still need to update the board"""
        increased = self.col + distance

        # move the car
        if self.orientation == 'H':
            self.col = increased
        if self.orientation == 'V':
            self.row = increased
