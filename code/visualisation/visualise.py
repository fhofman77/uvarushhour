import csv


def print_board(vehicles, board_size):
    for row in range(board_size):
        for col in range(board_size):
            printed = False
            for car in vehicles:
                if car.orientation == 'H':
                    for i in range(car.length):
                        if car.coordinate_row[0] == row+1 and car.coordinate_col[i] == col+1:
                            print(car.car, end=' ')
                            printed = True
                            continue
                else:
                    for i in range(car.length):
                        if car.coordinate_row[i] == row+1 and car.coordinate_col[0] == col+1:
                            print(car.car, end=' ')
                            printed = True
                            continue
            if printed == False:
                print('# ', end='')
                printed = True
        print('', end='\n')

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
