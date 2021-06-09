from code.classes.objects import Board, moves
from code.visualisation.visualise import print_board

inputdata = 'data/gameboards/Rushhour6x6_3.csv'
# Load all the vehicles

board = Board(inputdata)

for car in board.occupied_row_col:
    if car[0] == board.vehicles[1].car:
        print(car)

for car in board.occupied_row_col:
    if car[0] == board.vehicles[1].car:
        print(car)

print("\n Now we move impossible 20 spots back down")
board.move_car(board.vehicles[1], -2)
for car in board.occupied_row_col:
    if car[0] == board.vehicles[1].car:
        print(car)


board.print()
