import numpy as np
BOARD = np.zeros((8, 8))
def show_moves(moves):
    for row, col in moves:
        BOARD[row][col] = 2
