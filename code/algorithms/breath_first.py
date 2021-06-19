import queue
import copy
import time


def breath_algorithm(board):
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
        que = queue.Queue()
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


def depth_algorithm(board):
    start = time.time()

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
            end = time.time()
            print(end - start)
            return(solution)
        for state in all_states:
            if last_state[1] == state[0]:
                last_state = state


"""def depth_algorithm(board):
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
        visited = []
        loop = True
        alternatives = [child_states(board)]
        while loop:
            next_board = ((alternatives[-1])[-1])[0]
            # print(f'first {next_board}')
            print(len(alternatives))
            while next_board.occupied_row_col in visited:
                next_board = ((alternatives.pop(-1))[-1])[0]
                # print(next_board)
            if next_board.won_game():
                print('won')
                return
            else:
                # print(f'visited {visited}')
                visited.append(next_board.occupied_row_col)
                # print(f'child states {child_states(next_board)}')
                alternatives.append(child_states(next_board))
            
    
    solver(board)





def dfs_algorithm(board):
    def dfs_states(board):
        children = []
        for car in board.vehicles:
            for distance in range(-board.size + 1, board.size):
                if distance != 0:
                    current_board = copy.deepcopy(board)
                    if current_board.move_car(car, distance):
                        children.append(board)

        return children

    def dfs_search(start_state):
        queue = [[start_state]]
        seen_states = set()
        while queue:
            path = queue.pop()
            if path[-1].won_game():
                return True

            for next_state in dfs_states(path[-1]):
                if next_state not in seen_states:
                    seen_states.add(next_state)
                    queue.append(path + [next_state])
        return

    dfs_search(board)

    


"""
