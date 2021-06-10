import queue
import random
import copy

def breath_algorithm(board):
    def solver(new_state):
        que = queue.Queue()
        que.put(new_state)

    def all_states(board):
        original_board = copy.deepcopy(board)
        end_board = 0
        board.print()
        all_states = {}
        all_states['1'] = board.occupied_row_col
        print(all_states)
        board.move_car(board.vehicles[-1], -1)
        all_states['else'] = board.occupied_row_col
        print(all_states)
        board.print()

        
        # for i in range(200):
            
        #     if board not in all_states:
        #         print(board.occupied_row_col)
        #         all_states.append(board)
        #         if board.won_game():
        #             end_board = board
        
        # print(all_states)

        board = original_board
        return all_states, end_board
    
    all_states(board)
