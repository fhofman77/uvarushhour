moves = {
    'car': 'move'
}


class Board():
    def __init__(self, size, vehicles):
        # Columns run vertical (like a y axes)
        self.col = size
        # Rows run horizontal (like a x axes)
        self.row = size

    def winning_board(self):
        """Add Desired End Board"""
        # Last car of the csv-input is completely on the right side means it's WON
        pass

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
        self.cordinate_row = []
        self.cordinate_col = []

    def move(self, distance):
        # If the car is moved, append to moves dictionairy
        if distance != 0:
            moves[self.car] = distance

        """Still need to UPDATE BOARD && CHECK valid_move"""
        new_position = self.col + distance

        # Move the car
        if self.orientation == 'H':
            self.col = new_position
            self.cordinate_col = [i + distance for i in self.cordinate_col]
        if self.orientation == 'V':
            self.row = new_position
            self.cordinate_row = [i + distance for i in self.cordinate_col]

    def valid_move(self):
        """Return true is a move is possible otherwise return false?"""
        # For every car check what spaces are occupied.
        # If the move is not passing over any of these spaces return true
        
        pass
