from code.visualisation.visualise import visualiser
from code.classes.objects import moves
import csv

# Load all the vehicles
vehicles = visualiser()

vehicles[0].move(1)
vehicles[2].move(-3)
print(f"Moves: {moves}")

# Creates a CSV file from all the moves that have been added to the dict
with open('data/output/output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in moves.items():
        writer.writerow([key, value])
