import csv
from ..classes.objects import Car

def visualise():
    vehicles = []
    with open('/Users/frank/Documents/UVA 2020:2021/Programmeren/programeer theorie/uvarushhour/data/gameboards/Rushhour6x6_1.csv', newline='') as gamefile:
        rows = csv.reader(gamefile, delimiter=',')
        next(rows)
        count = 0
        for row in rows:
            vehicle = Car(row[0], row[1], row[2], row[3], row[4])
            vehicles.append(vehicle)

    for row in range(5):
        for col in range(5):
        #     print('# ', end='')
        # print()
            for car in range(len(vehicles)):
                if int(col + 1) == int(vehicles[car].col) and int(row + 1) == int(vehicles[car].row):
                    print(vehicles[car].car, end='')
                else:
                    print('*', end='')
        print()
    

