from code.classes.objects import moves
from code.visualisation.visualise import initialize_cars, get_board_size, print_board
inputdata = 'data/gameboards/Rushhour6x6_1.csv'
# Load all the vehicles
vehicles = initialize_cars(inputdata)
print_board(vehicles, get_board_size(inputdata))

Car.move
print_board()