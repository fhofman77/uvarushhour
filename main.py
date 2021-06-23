from code.algorithms.random import random_move
from code.algorithms.breadth_depth import BFS_DFS
from code.visualisation.visualise import create_csv
from code.classes.objects import Board

inputdata = 'data/gameboards/Rushhour6x6_1.csv'
board = Board(inputdata)

algorithm = input('Choose an algorithm: breadth, depth or random\n')
game = (inputdata.split('/'))[-1]

if algorithm == 'breadth' or algorithm == 'depth':
    moves = BFS_DFS(board, algorithm)
    create_csv(moves, algorithm, game)
elif algorithm == 'random':
    moves = []
    while not board.won_game():
        move = random_move(board)
        if move:
            moves.append(move)
    create_csv(moves, algorithm, game)
else:
    print('Choose a correct algorithm: breadth, depth or random')
