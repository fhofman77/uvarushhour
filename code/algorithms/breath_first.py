import queue
import random
import copy

def breath_algorithm(board):
    def solver(new_state):
        que = queue.Queue()
        que.put(new_state)

    def all_states(board):
        original_board = copy.deepcopy(board)
        states = {}
        all_states = []
        for last_state in all_states:
            
            for car in board.vehicles:
                for distance in range(-board.size + 1, board.size - 1):
                    if board.move_car(car, distance):
                        board.print()
                        all_states.append(board.occupied_row_col)
                        last_state
        # print(all_states)



        
        # for i in range(200):
            
        #     if board not in all_states:
        #         print(board.occupied_row_col)
        #         all_states.append(board)
        #         if board.won_game():
        #             end_board = board
        
        # print(all_states)

        board = original_board
        return all_states
    
    all_states(board)
