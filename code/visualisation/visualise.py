import csv
import re
from ..classes.objects import Car, moves


def get_board_size(inputdata):
    """Finds the value between 'Rushhour' and 'x' and returns it as an int"""
    board_size = re.search('Rushhour(.*)x', inputdata)
    board_size = int((board_size.group(1)))
    return board_size


def print_board(vehicles, board_size):
    for row in range(board_size):
        for col in range(board_size):
            printed = False
            for car in vehicles:
                if car.orientation == 'H':
                    for i in range(car.length):
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
            if printed == False:
                print('# ', end='')
                printed = True
        print('', end='\n')


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

    return vehicles

    # Beter om elke voor car een occupied spaces variabele aan te maken?
    # Example: Car 1: occupied-row: [4], occupied col =[3,4,5]?
    # Print car name if the row we are in == the occupied row of a car && col == occupied col
    # Else print *
    # Deze kunnen we dan ook gebruiken om te checken of een move kan


def create_csv(moves):
    """Creates a CSV file from all the moves that have been added to a dict"""
    with open(f'data/output/output{moves}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in moves.items():
            writer.writerow([key, value])
