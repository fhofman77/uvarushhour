from code.classes.objects import moves
from code.visualisation.visualise import initialize_cars, get_board_size, print_cars
from code.visualisation.visualise import initialize_cars, get_board_size, print_board
<< << << < Updated upstream
== == == =
>>>>>> > Stashed changes
inputdata = 'data/gameboards/Rushhour6x6_1.csv'
# Load all the vehicles
vehicles = initialize_cars(inputdata)

vehicles[0].move(1)
vehicles[2].move(-3)
print_cars(vehicles, get_board_size(inputdata))
