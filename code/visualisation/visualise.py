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

    occupied_coordinates = []
    for car in vehicles:
        if car.orientation == 'H':
            x = car.row
            for i in range(int(car.length)):
                y = car.col
                # print(f'y = {y} and i = {i}')
                y += i
                car_coordinates = [x, y]
                occupied_coordinates.append(car_coordinates)
        else:
            y = car.row
            for i in range(int(car.col)):
                x = car.col
                # print(f'y = {y} and i = {i}')
                x += i
                car_coordinates = [x, y]
                occupied_coordinates.append(car_coordinates)
    print(occupied_coordinates)
            
            

    for row in range(6):
        for col in range(6):
            printed = False
            for i in occupied_coordinates:
                if i[0] != row and i[1] != col and not printed:
                    print('# ', end='')
                    printed = True
                elif not printed:
                    print('* ', end='')
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
