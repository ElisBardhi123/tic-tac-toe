from model import Board
import controller

def start_game(board):
    controller.print_board(board)
    while True:
        user_input = controller.get_user_input(board)
        if user_input:
            x,y = controller.num_to_cord(board, user_input)
            if controller.check_input_valid(board, x, y):
                board[x][y].setContent('X')
                if controller.check_winner(board, 'X'):
                    break
                controller.bot_move(board)
                controller.print_board(board)
                if controller.check_winner(board, 'O'):
                    break
            else:
                print('Invalid Input: Try again')
        else:
            print('Invalid Input: Try again')


board = Board(shape=3).get_board()
start_game(board)