from code.classes.objects import Car
from ..visualisation.visualise import visualise
import csv
moves = []


def move(car, distance):
    # if the car is moved, append to moves
    if distance != 0:
        moves.append(f'{car.car},{distance}')
    
    increased = int(car.col) + distance

    # move the car
    if car.orientation == 'H':
        car.col = increased
    if car.orientation == 'V':
        car.row = increased

    return car

vehicles = visualise()

print(vehicles[0])
# move(vehicles[0], 1)
# print(moves)
