import numpy as np
import random

'''
Example: board with shape 3x3

[1,2,3] 
[4,5,6] 
[7,8,9]
                    
'''

def get_board_shape():
    size = int(input("Select Tic-Tac-Toe Size: "))
    return size

def num_to_cord(user_input):
    x = int(np.ceil(user_input / shape) - 1)
    y = (user_input + (shape - 1)) % shape
    return (x,y)

def check_input_valid(cordinate):
    if board[cordinate] != 0:
        return False
    return True

def get_user_input():
    user_input = int(input("Select a number: "))
    if user_input <= shape*shape:
        return user_input

def check_rows():
    for row in board:
        if len(set(row)) <= 1 and 0 not in row:
            return True

def check_columns():
    for index in range(shape):
        column = [row[index] for row in board]
        if len(set(column)) <= 1 and 0 not in column:
            return True
    return False

def check_diagonals():
    first_diagonal = [board[i,i] for i in range(shape)]
    second_diagonal = [board[i,shape-1-i] for i in range(shape)]
    if ( len(set(first_diagonal)) <= 1 and 0 not in first_diagonal) or ( len(set(second_diagonal)) <= 1 and 0 not in second_diagonal):
        return True
    return False

def check_winner(player):
    if check_rows() or check_columns() or check_diagonals():
        print(f'Player {player} won')
        return True
    return False

def print_board():
    for row in board:
        edited_row = '|'.join(list(map(str, row)))
        print(edited_row)
        print('_' * len(edited_row))

def get_valid_moves():
    iter = 1
    result = []
    for row in board:
        for i in row:
            if i == 0:
              result.append(iter)
            iter = iter + 1
    return result

def bot_move():
    valid_moves = get_valid_moves()
    random_move = random.choice(valid_moves)
    cordinate = num_to_cord(random_move)
    board[cordinate] = 2


shape = get_board_shape()
board = np.zeros((shape,shape))

game_on = True

while game_on:
    user_input = get_user_input()
    if user_input:
        cordinate = num_to_cord(user_input)
        if check_input_valid(cordinate):
            board[cordinate] = 1
            if check_winner(1):
                break
            bot_move()
            print_board()
            if check_winner(2):
                break
        else:
            print('Invalid Input: Try again')
    else:
        print('Invalid Input: Try again')

print()
print_board()
#if __name__ = '__main__ ':
