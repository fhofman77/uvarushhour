from code.classes.objects import moves
from code.visualisation.visualise import initialize_cars, get_board_size, print_board

inputdata = 'data/gameboards/Rushhour6x6_1.csv'
# Load all the vehicles
print(get_board_size(inputdata))
vehicles = initialize_cars(inputdata)

vehicles[0].move(1)
vehicles[2].move(-3)
print_board(vehicles, get_board_size(inputdata))


