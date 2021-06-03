from code.classes.objects import Car
from ..visualisation.visualise import visualise
import csv
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


vehicles = []
with open('data/gameboards/Rushhour6x6_1.csv', newline='') as gamefile:
    rows = csv.reader(gamefile, delimiter=',')
    next(rows)
    count = 0
    for row in rows:
        vehicle = Car(row[0], row[1], row[2], row[3], row[4])
        vehicles.append(vehicle)

print(vehicles[0])
move(vehicles[0], 1)
print(moves)
