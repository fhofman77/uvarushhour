from code.algorithms.random import random_move
from code.algorithms.breadth_depth import BFS_DFS
from code.visualisation.visualise import create_csv
from code.classes.objects import Board, moves

inputdata = 'data/gameboards/Rushhour6x6_1.csv'
board = Board(inputdata)

# algorithm = 'breadth'
# moves = BFS_DFS(board, algorithm)
game = (inputdata.split('/'))[-1]

# create_csv(moves, algorithm, game)

algorithm = 'random'
moves = []
while not board.won_game():
    move = random_move(board)
    if move:
        moves.append(move)
create_csv(moves, algorithm, game)
