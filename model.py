import numpy as np
from tile import Tile

class Board:
    def get_board(self):
        return self.board

    def get_board_shape(self):
        size = int(input("Select Tic-Tac-Toe Size: "))
        return size
    
    def create_board(self, shape):
        board = [[0 for _ in range(shape)] for _ in range(shape)]
        iter = 1
        for i in range(shape):
            for j in range(shape):
                board[i][j] = Tile(iter)
                iter = iter + 1
        return board

    def getLength(self):
        return len(self.board)

    def __init__(self, shape=None):
        if not shape:
            shape = self.get_board_shape()
        self.board = self.create_board(shape)
