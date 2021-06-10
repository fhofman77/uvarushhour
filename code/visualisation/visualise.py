import csv

""" versie waar het object word meegegeven
def print_board(occupied_row_col, board_size):
    for row in range(board_size):
        for col in range(board_size):
            not_printed = True
            for car in occupied_row_col:
                if car[1] == row+1 and car[2] == col+1:
                    print(car[0].car, end=' ')
                    not_printed = False
            
            if not_printed:
                print('# ', end='')
                not_printed = False
        print('')
"""

""" versie waar car word meegegeven op de eerste plek """


def print_board(occupied_row_col, board_size):
    for row in range(board_size):
        for col in range(board_size):
            not_printed = True
            for car in occupied_row_col:
                if car[1] == row+1 and car[2] == col+1:
                    print(car[0], end=' ')
                    not_printed = False

            if not_printed:
                print('# ', end='')
                not_printed = False
        print('')


def create_csv(moves):
    """Creates a CSV file from all the moves that have been added to a dict"""
    with open(f'data/output/output{moves}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in moves.items():
            writer.writerow([key, value])
