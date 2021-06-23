from code.algorithms.algorithm import random_move, BFS_DFS
from code.classes.objects import Board
from code.visualisation.visualise import create_csv
import sys

# Choose a gameboard. Then run the file
inputdata = 'data/gameboards/Rushhour6x6_1.csv'
"""
A prompt will ask what algorithm you would like to use, the solution can then be found in the data/output folder
"""
board = Board(inputdata)

algorithm = input('Choose an algorithm: breadth, depth or random\n')
game = (inputdata.split('/'))[-1]

if algorithm == 'breadth' or algorithm == 'depth':
    moves = BFS_DFS(board, algorithm)
    create_csv(moves, algorithm, game)
elif algorithm == 'random':
    sys.stdout.write('\rloading...')
    moves = []
    while not board.won_game():
        move = random_move(board)
        if move:
            moves.append(move)
    sys.stdout.write('\rDone!     \n')
    create_csv(moves, algorithm, game)
else:
    print('Choose a correct algorithm: breadth, depth or random')
