import queue
import copy

def breath_algorithm(board):

    def child_states(board):
        children = []
        print(f'this is board {board}')
        board = board[1]
        for car in board.vehicles:
            for distance in range(-board.size + 1, board.size - 1):
                current_board = copy.deepcopy(board)
                if distance == 0:
                    continue
                if current_board.move_car(car, distance):
                    print('good')
                    current_board.print()
                    route = [board, current_board, car.car, distance]
                    children.append(route)

            print(car.car)
        print(children)

        return children

    def solver(board):
        que = queue.Queue()
        visited = []
        que.put([0, board])

        while not que.empty():
            next_board = que.get()
            # next_board = object_list.keys
            print(next_board)
            children = child_states(next_board)
            for child in children:
                print(f'child {child}')
                print(f'visited {visited}')
                print(child not in visited)
                if child not in visited:
                    que.put(children)
                    visited.append(children)
                    print(f'test: {que}')
                else:
                    print('not')
        return

    
    solver(board)


