import queue
import copy

def breath_algorithm(board):

    def child_states(list):
        children = []
        print(f'this is board {list}')
        board = list
        # print(f'this is board {board}')
        board.print()
        for car in board.vehicles:
            for distance in range(-board.size + 1, board.size):
                if distance != 0:
                    print(distance)
                    current_board = copy.deepcopy(board)
                    # print(current_board.move_car(car, distance))
                    if current_board.move_car(car, distance):
                        print('good')
                        # current_board.print()
                        route = [current_board, board, car.car, distance]
                        children.append(route)

            print(car.car)
            print(children)
            # return children
            
        # print(f'childeren: {children}')

        return children

    def solver(board):
        que = queue.Queue()
        visited = []
        que.put([[board, board]])
        visisted_printer = []
        count = 0
        cycle = 0

        while not que.empty():
            cycle+=1
            temp = que.get()
            # print(f'this is temp {temp}')
            next_board = temp
            print(f'this is next board in solver {next_board}')
            children = child_states(next_board)
            for child in children:
                if child[0].won_game():
                    print('won')
                    return
                if child[0].occupied_row_col not in visited:
                    # print(f'what is put {child}')
                    que.put(child[0])
                    print(f'waht is put in que {child[0].occupied_row_col}')
                    visited.append(child[0].occupied_row_col)
                    visisted_printer.append(child[0])
                    count+=1
                else:
                    # print('not')
                    pass

        print('this is visited')

        print(count)
        
        count = 1
        for board in visisted_printer:
            print(count)
            board.print()
            count +=1
        
        print(f'total cycle: {cycle}')

        return

    
    solver(board)


