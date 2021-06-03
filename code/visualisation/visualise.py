import csv
from ..classes.objects import Car

def visualise():
    vehicles = []
    with open('data/gameboards/Rushhour6x6_1.csv', newline='') as gamefile:
        rows = csv.reader(gamefile, delimiter=',')
        next(rows)
        for row in rows:
            vehicle = Car(row[0], row[1], row[2], row[3], row[4])
            vehicles.append(vehicle)

    for row in range(6):
        for col in range(6):
            printed = False
            for car in range(len(vehicles)):
                if int(col + 1) == int(vehicles[car].col) and int(row + 1) == int(vehicles[car].row):
                    print(f'{vehicles[car].car} ', end='')
                    printed = True
                    if vehicles[car].orientation == 'H':
                        print(f'{vehicles[car].car} ', end='')
                        col += 1
                        if int(vehicles[car].length) == 3:
                            print(f'{vehicles[car].car} ', end='')
                            col += 1
            if not printed:    
                print('# ', end='')
        print()

        return vehicles
    

