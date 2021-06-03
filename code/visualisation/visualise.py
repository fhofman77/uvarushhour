import csv
from .code import Car


with open('/Users/frank/Documents/UVA 2020:2021/Programmeren/programeer theorie/uvarushhour/data/gameboards/Rushhour6x6_1.csv', newline='') as gamefile:
    rows = csv.reader(gamefile, delimiter=',')
    next(rows)
    for row in rows:
        Car(row[0], row[1], row[2], row[3], row[4])
        print(Car.id)
    

