from piece import ChessPiece
import numpy as np
from moves import Moves
import pygame
# BOARD = np.zeros((8, 8))

class Rook(ChessPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        if self.color == 'w':
            img_path = 'images/white_r.png'
            self.img = pygame.image.load(img_path)
        else:
            img_path = 'images/black_r.png'
            self.img = pygame.image.load(img_path)
            



    def update_pos(self, row, col):
        self.col = col
        self.row = row 
    


    def get_moves(self, BOARD):
        """
        Returns a list of valid moves for the rook at the given row and column
        on the given board.
        """
        valid_moves = Moves(self.row, self.col).horizontal_vertical(self.color, BOARD)
        return valid_moves

    def __str__(self):
        """
        Returns a string representation of the rook.
        """
        if self.color == "w":
            return "♖"
        else:
            return "♜" 

    def __repr__(self) -> str:
        return self.color + 'r'

def main():
    pass


if __name__ == "__main__":
    main()


