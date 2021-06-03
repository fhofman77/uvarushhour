moves = []

def move(Car, distance):
    # if the car is moved, append to moves
    if distance != 0:
        moves.append(Car, distance)

    # move the car
    if Car.orientation == 'H':
        Car.col += distance
    if Car.orientation == 'V':
        Car.row += distance

    return Car