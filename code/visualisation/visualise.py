import csv
from ..classes.objects import Car, moves


def visualiser():
    vehicles = []
    with open('data/gameboards/Rushhour6x6_1.csv', newline='') as gamefile:
        rows = csv.reader(gamefile, delimiter=',')
        next(rows)
        for row in rows:
            vehicle = Car(row[0], row[1], row[2], row[3], row[4])
            vehicles.append(vehicle)

    # Dit werkt nu niet voor boards met een andere size dan 6, ook klopt de logica niet
    for row in range(6):
        for col in range(6):
            """ 
            Beter om elke voor car een occupied spaces variabele aan te maken?
            Example: Car 1: occupied-row: [4], occupied col =[3,4,5]?
            Print car name if the row we are in == the occupied row of a car && col == occupied col
            Else print *
            Deze kunnen we dan ook gebruiken om te checken of een move kan
            """
            printed = False
            for car in range(len(vehicles)):
                if col + 1 == vehicles[car].col and row + 1 == vehicles[car].row:
                    print(f'{vehicles[car].car} ', end='')
                    printed = True
                    if vehicles[car].orientation == 'H':
                        print(f'{vehicles[car].car} ', end='')
                        col += 1
                        if vehicles[car].length == 3:
                            print(f'{vehicles[car].car} ', end='')
                            col += 1
            if not printed:
                print('# ', end='')
        print()

        return vehicles
