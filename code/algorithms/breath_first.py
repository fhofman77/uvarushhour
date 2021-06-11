import queue
import copy

def breath_algorithm(board):

    def child_states(list):
        children = []
        print(f'this is board {list}')
        # board = list[1]
        # print(f'this is board {board}')
        for car in board.vehicles:
            for distance in range(-board.size + 1, board.size):
                if distance != 0:
                    print(distance)
                    current_board = copy.deepcopy(board)
                    print(current_board.move_car(car, distance))
                    if current_board.move_car(car, distance):
                        # print('good')
                        # current_board.print()
                        route = [current_board, board, car.car, distance]
                        children.append(route)

            print(car.car)
            print(children)
        print(f'childeren: {children}')

        return children

    def solver(board):
        que = queue.Queue()
        visited = []
        que.put([[board, board]])

        while not que.empty():
            temp = que.get()
            print(f'this is temp {temp}')
            next_board = temp[0]
            print(f'this is next board in solver {next_board}')
            children = child_states(next_board)
            for child in children:
                if child[0].won_game():
                    print('won')
                    return
                # print(f'child {child[0]}')
                # print(f'child not in {visited}')
                if child[0].occupied_row_col not in visited:
                    print(f'what is put {child}')
                    que.put(child)
                    visited.append(child[0].occupied_row_col)
                    # print(f'test: {que}')
                else:
                    print('not')
            print(que.qsize())
        print('this is visited')
        print(visited)
        return

    
    solver(board)


