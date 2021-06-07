from code.classes.objects import moves
from code.visualisation.visualise import initialize_cars, get_board_size, print_board
inputdata = 'data/gameboards/Rushhour6x6_1.csv'
# Load all the vehicles
vehicles = initialize_cars(inputdata)
print_board(vehicles, get_board_size(inputdata))


vehicles[0].move(1)
vehicles[2].move(-3)
print(f"Moves: {moves}")

# Creates a CSV file from all the moves that have been added to the dict
with open('data/output/output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in moves.items():
        writer.writerow([key, value])


a = get_board_size(inputdata)
print_board(a, vehicles)
=======
Car.move
print_board()

