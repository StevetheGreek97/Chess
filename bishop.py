from piece import ChessPiece
import numpy as np
import pygame
from moves import Moves

class Bishop(ChessPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        if self.color == 'w':
            img_path = 'images/white_b.png'
            self.img = pygame.image.load(img_path)
        else:
            img_path = 'images/black_b.png'
            self.img = pygame.image.load(img_path)
            

    def get_moves(self, board):
        """
        Returns a list of valid moves for the bishop at the given row and column
        on the given board.
        """
        valid_moves = []
        valid_moves += Moves(self.row, self.col).diagonal(self.color, board)
        return valid_moves

    def __str__(self):
        """
        Returns a string representation of the bishop.
        """
        if self.color == "w":
            return "♗"
        else:
            return "♝"
        
    def __repr__(self) -> str:
        return self.color + 'b'

def main():
    pass


if __name__ == "__main__":
    main()

