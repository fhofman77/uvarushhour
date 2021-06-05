from code.visualisation.visualise import initialize_cars, get_board_size
from code.classes.objects import moves
import csv

inputdata = 'data/gameboards/Rushhour12x12_7.csv'
# Load all the vehicles
vehicles = initialize_cars(inputdata)

vehicles[0].move(1)
vehicles[2].move(-3)
print(f"Moves: {moves}")

# Creates a CSV file from all the moves that have been added to the dict
with open('data/output/output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in moves.items():
        writer.writerow([key, value])


a = get_board_size(inputdata)
print(a)
