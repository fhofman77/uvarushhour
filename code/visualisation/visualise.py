import csv
import re
from ..classes.objects import Car, moves


def get_board_size(inputdata):
    """Finds the value between 'Rushhour' and 'x' and returns it as an int"""
    board_size = re.search('Rushhour(.*)x', inputdata)
    return int((board_size.group(1)))


def initialize_cars(csv_input):
    vehicles = []
    with open(csv_input, newline='') as gamefile:
        rows = csv.reader(gamefile, delimiter=',')
        next(rows)
        for row in rows:
            vehicle = Car(row[0], row[1], row[2], row[3], row[4])
            vehicles.append(vehicle)

    # Printen misschien beter in een andere functie
    # Dit werkt nu niet voor boards met een andere size dan 6, ook klopt de logica niet

    for car in vehicles:
        if car.orientation == 'H':
            car.cordinate_row = car.row
            for i in range(int(car.length)):
                y = car.col
                y += i
                car.cordinate_col.append(y)
        else:
            car.cordinate_col = car.col
            for i in range(int(car.length)):
                x = car.row
                x += i
                car.cordinate_row.append(x)
        print(car.car, car.cordinate_row, car.cordinate_col)

    for row in range(get_board_size(csv_input)):
        for col in range(get_board_size(csv_input)):
            printed = False
            for car in vehicles:
                if car.orientation == 'H':
                    for i in range(car.length):
                        # print(f'loop {car.cordinate_col[i]}', end='')
                        # print(f'not loop {col+1}, row {row+1}, car row {car.cordinate_row}')
                        if car.cordinate_row == row+1 and car.cordinate_col[i] == col+1:
                            print(car.car, end=' ')
                            printed = True
                            continue
                else:
                    for i in range(car.length):
                        if car.cordinate_row[i] == row+1 and car.cordinate_col == col+1:
                            print(car.car, end=' ')
                            printed = True
                            continue
                        # elif printed == False and i == len(car.cordinate_row)-1:
                        #     print('# ', end='')
                        #     printed = True
            if printed == False:
                print('# ', end='')
                printed = True

        print('', end='\n')

        # """
        # Beter om elke voor car een occupied spaces variabele aan te maken?
        # Example: Car 1: occupied-row: [4], occupied col =[3,4,5]?
        # Print car name if the row we are in == the occupied row of a car && col == occupied col
        # Else print *
        # Deze kunnen we dan ook gebruiken om te checken of een move kan
        # """
        #     printed = False
        #     for car in range(len(vehicles)):
        #         if col + 1 == vehicles[car].col and row + 1 == vehicles[car].row:
        #             print(f'{vehicles[car].car} ', end='')
        #             printed = True
        #             if vehicles[car].orientation == 'H':
        #                 print(f'{vehicles[car].car} ', end='')
        #                 col += 1
        #                 if vehicles[car].length == 3:
        #                     print(f'{vehicles[car].car} ', end='')
        #                     col += 1
        #     if not printed:
        #         print('# ', end='')
        # print()

    return vehicles
