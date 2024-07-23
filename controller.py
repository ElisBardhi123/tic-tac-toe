import numpy as np
import random

def num_to_cord(board, user_input):
    shape = len(board)
    x = int(np.ceil(user_input / shape) - 1)
    y = (user_input + (shape - 1)) % shape
    return x,y

def check_input_valid(board, x, y):
    if board[x][y].content == 'X' or board[x][y].content == 'O':
        return False
    return True

def get_user_input(board):
    user_input = int(input("Select a number: "))
    if user_input <= len(board)**2:
        return user_input

def check_rows(board):
    for row in board:
        row_content = [i.content for i in row]
        if len(set(row_content)) <= 1 and 0 not in row_content:
            return True

def check_columns(board):
    for index in range(len(board)):
        column = [row[index].content for row in board]
        if len(set(column)) <= 1 and 0 not in column:
            return True
    return False

def check_diagonals(board):
    shape = len(board)
    first_diagonal = [board[i][i].content for i in range(shape)]
    second_diagonal = [board[i][shape-1-i].content for i in range(shape)]
    if ( len(set(first_diagonal)) <= 1 and 0 not in first_diagonal) or ( len(set(second_diagonal)) <= 1 and 0 not in second_diagonal):
        return True
    return False

def check_winner(board, player):
    if check_rows(board) or check_columns(board) or check_diagonals(board):
        print(f'Player {player} won')
        print_board(board)
        return True
    return False

def get_valid_moves(board):
    iter = 1
    result = []
    for row in board:
        for i in row:
            if i.content != 'X' and i.content != 'O':
              result.append(iter)
            iter = iter + 1
    return result

def bot_move(board):
    valid_moves = get_valid_moves(board)
    random_move = random.choice(valid_moves)
    x,y = num_to_cord(board, random_move)
    board[x][y].setContent('O')


def print_board(board):
    for row in board:
        edited_row = '|'.join(list(map(str, row)))
        print(edited_row)
        print('_' * len(edited_row))