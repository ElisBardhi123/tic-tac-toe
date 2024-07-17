import numpy as np

class Board:

    def get_board_shape(self):
        size = int(input("Select Tic-Tac-Toe Size: "))
        return size
    
    def create_board(self, shape):
        board = np.zeros((shape,shape))
        iter = 1
        for i in range(shape):
            for j in range(shape):
                board[i][j] = iter
                iter = iter + 1
        return board
    
    def print_board(self):
        for row in self.board:
            edited_row = '|'.join(list(map(str, row)))
            print(edited_row)
            print('_' * len(edited_row))

    def __init__(self, shape=None):
        if not shape:
            shape = self.get_board_shape()
        self.board = self.create_board(shape)