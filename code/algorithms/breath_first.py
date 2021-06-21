import queue
import copy
import time


def BFS_DFS(board, search_method):
    def child_states(board):
        children = []
        for car in board.vehicles:
            for distance in range(-board.size + 1, board.size):
                if distance != 0:
                    child_board = copy.deepcopy(board)
                    if child_board.move_car(car, distance):
                        route = [child_board, board, car.car, distance]
                        children.append(route)

        return children

    def solver(board, search_method):
        if search_method.lower() == 'depth' or search_method.lower() == "d":
            """If the user specifies depth first search method, usef LifoQueue"""
            que = queue.LifoQueue()
        elif search_method.lower() == 'breadth' or search_method.lower() == "b":
            """Otherwise use breadthfirst search"""
            que = queue.Queue()
        else:
            print('Enter a correct search method using breadth, depth, b or d')
        visited = []
        que.put([board, board])
        all_states = []

        while not que.empty():
            next_board = que.get()
            children = child_states(next_board[0])
            for child in children:
                if child[0].won_game():
                    print('won')
                    all_states.append(child)
                    return all_states
                if child[0].occupied_row_col not in visited:
                    que.put(child)
                    visited.append(child[0].occupied_row_col)
                    all_states.append(child)

        print('Could not find solution')
        return

    solution = []
    all_states = solver(board, search_method)
    last_state = all_states.pop(-1)
    loop = True
    # while last_state[1].occupied_row_col != board.occupied_row_col:
    while loop:
        solution.append([last_state[2], last_state[3]])
        if last_state[1].occupied_row_col == board.occupied_row_col:
            solution.reverse()
            solution.insert(0, ['car', 'move'])
            print(solution)
            return(solution)
        for state in all_states:
            if last_state[1] == state[0]:
                last_state = state

"""
# test of itterative deepening
def iterative_deepening(board):
    def child_states(board):
        children = []
        for car in board.vehicles:
            for distance in range(-board.size + 1, board.size):
                if distance != 0:
                    child_board = copy.deepcopy(board)
                    if child_board.move_car(car, distance):
                        route = [child_board, board, car.car, distance]
                        children.append(route)

        return children

    def solver(board):
        que = queue.LifoQueue()
        visited = []
        que.put([board, board])
        all_states = []
        counter = 0

        while not que.empty() and counter < 300:
            next_board = que.get()
            children = child_states(next_board[0])
            counter+=1
            for child in children:
                if child[0].won_game():
                    print('won')
                    all_states.append(child)
                    return all_states
                if child[0].occupied_row_col not in visited:
                    que.put(child)
                    visited.append(child[0].occupied_row_col)
                    all_states.append(child)

        print('Could not find solution')
        return

    solution = []
    all_states = solver(board)
    last_state = all_states.pop(-1)
    loop = True
    # while last_state[1].occupied_row_col != board.occupied_row_col:
    while loop:
        solution.append([last_state[2], last_state[3]])
        if last_state[1].occupied_row_col == board.occupied_row_col:
            solution.reverse()
            solution.insert(0, ['car', 'move'])
            print(solution)
            return(solution)
        for state in all_states:
            if last_state[1] == state[0]:
                last_state = state

    solver(board)
"""