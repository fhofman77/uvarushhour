import queue
import copy

def breath_algorithm(board):

    def child_states(board):
        children = []
        for car in board.vehicles:
            for distance in range(-board.size + 1, board.size):
                if distance != 0:
                    current_board = copy.deepcopy(board)
                    if current_board.move_car(car, distance):
                        route = [current_board, board, car.car, distance]
                        children.append(route)

        return children

    def solver(board):
        que = queue.Queue()
        visited = []
        que.put([board, board])

        while not que.empty():
            temp = que.get()
            if que.qsize != 1:
                next_board = temp[0]
            next_board = temp
            children = child_states(next_board[0])
            for child in children:
                if child[0].won_game():
                    return
                if child[0].occupied_row_col not in visited:
                    que.put(child)
                    visited.append(child[0].occupied_row_col)
 
        return

    
    solver(board)


