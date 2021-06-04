moves = {
    'car': 'move'
}


class Board():
    def __init__(self, size):
        # columns run vertical (like a y axes)
        self.col = size
        # rows run horizontal (like a x axes)
        self.row = size

    def end_board(self):
        """Add Desired End Board"""
        # Last car on the list is completely on the right side
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

    def valid_move(self):
        """Return true is a move is possible otherwise return false?"""
        # For every car check what spaces are occupied.
        # If the move is not passing over any of these spaces return true
        pass
