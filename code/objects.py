from code.visualising import visualise

moves = []


class Board():
    def __init__(self, size):
        # columns run vertical (like a y axes)
        self.col = size
        # rows run horizontal (like a x axes)
        self.row = size


class Car():
    def __init__(self, car, orientation, col, row, length):
        # in the data the last car is the car that needs to escape
        self.car = car
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length
        self.moves = []

    def move(self, distance):
        # if the car is moved, append to moves
        if distance != 0:
            moves.append(f'{self.car},{distance}')

        increased = self.col + distance

        # move the car
        if self.orientation == 'H':
            self.col = increased
        if self.orientation == 'V':
            self.row = increased


Horizontal = Car("Horizontal Move", "H", 4, 1, 3)


vehicles = visualise()

print(vehicles[0])
vehicles[0].move(vehicles[0], 1)
print(moves)
