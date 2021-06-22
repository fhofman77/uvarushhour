import queue
import copy

"""
A function where you can to apply a breadth of depth first algorithm
"""
def BFS_DFS(board, search_method):
    """
    Creates the child states for a given board_state.
    """
    def child_states(board):
        children = []
        # move every car all possibble places in the board
        for car in board.vehicles:
            for distance in range(-board.size + 1, board.size):
                if distance != 0:
                    child_board = copy.deepcopy(board)
                    # if the car is abble to move append the new state to the list
                    if child_board.move_car(car, distance):
                        route = [child_board, board, car.car, distance]
                        children.append(route)

        return children
    
    """
    function that tries to solve the board in a breadth or depth first search algorithm
    """
    def solver(board, search_method):
        # check what algorithm is chosen to select the right que type
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

        # keep running wile the que is not empty
        while not que.empty():
            print(que.qsize())
            next_board = que.get()
            children = child_states(next_board[0])
            for child in children:
                # take the first state in que and check if it has won
                if child[0].won_game():
                    print('won')
                    all_states.append(child)
                    return all_states
                # if not won and the state the state not in visited the child state is set in the que and is visited
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
    while loop:
        # Save every stape made to go to the parrent state
        solution.append([last_state[2], last_state[3]])
        # If the board state is the same as the original board state return the solution
        if last_state[1].occupied_row_col == board.occupied_row_col:
            solution.reverse()
            solution.insert(0, ['car', 'move'])
            print(solution)
            return(solution)
        # Look for the parent state in all states so the next itteration the move can be saved
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