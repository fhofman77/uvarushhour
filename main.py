<<<<<<< HEAD
from code.classes.objects import moves
from code.visualisation.visualise import initialize_cars, get_board_size, print_cars
from code.visualisation.visualise import initialize_cars, get_board_size, print_board
<< << << < Updated upstream
== == == =
>>>>>> > Stashed changes
=======
from code.visualisation.visualise import initialize_cars, get_board_size, print_board
from code.classes.objects import moves
import csv

>>>>>>> parent of a9d7519 (Merge branch 'main' into frank)
inputdata = 'data/gameboards/Rushhour6x6_1.csv'
# Load all the vehicles
vehicles = initialize_cars(inputdata)

vehicles[0].move(1)
vehicles[2].move(-3)
<<<<<<< HEAD
print_cars(vehicles, get_board_size(inputdata))
=======
print(f"Moves: {moves}")

# Creates a CSV file from all the moves that have been added to the dict
with open('data/output/output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in moves.items():
        writer.writerow([key, value])


a = get_board_size(inputdata)
print_board(a, vehicles)
>>>>>>> parent of a9d7519 (Merge branch 'main' into frank)
