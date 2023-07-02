from piece import ChessPiece
import numpy as np
import pygame
from moves import Moves

class Queen(ChessPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        if self.color == 'w':
            img_path = 'images/white_q.png'
            self.img = pygame.image.load(img_path)
        else:
            img_path = 'images/black_q.png'
            self.img = pygame.image.load(img_path)
            


    def get_moves(self, board):
        """
        Returns a list of valid moves for the queen at the given row and column
        on the given board.
        """
        valid_moves = []
        valid_moves += Moves(self.row, self.col).diagonal(self.color, board)
        valid_moves += Moves(self.row, self.col).horizontal_vertical(self.color, board)
        return valid_moves

    def __str__(self):
        """
        Returns a string representation of the queen.
        """
        if self.color == "w":
            return "♕"
        else:
            return "♛"

    def __repr__(self) -> str:
        return self.color + 'q'
        


def main():
    pass


if __name__ == "__main__":
    main()

