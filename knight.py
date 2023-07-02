import numpy as np
from piece import ChessPiece
from moves import Moves
import pygame


class Knight(ChessPiece):

    def __init__(self, color, row, col):
        super().__init__(color,row, col)
        if self.color == 'w':
            img_path = 'images/white_n.png'
            self.img = pygame.image.load(img_path)
        else:
            img_path = 'images/black_n.png'
            self.img = pygame.image.load(img_path)
            

        # Define the possible offsets for the knight's moves
        self.offsets = np.array([
            (2,1), 
            (1,2), 
            (-1,2), 
            (-2,1), 
            (-2,-1), 
            (-1,-2), 
            (1,-2), 
            (2,-1)
])



    def get_moves(self, board):
        """
        Returns a list of valid moves for the knight at the given row and column
        on the given board.
        """
        valid_moves = Moves(self.row, self.col).knights_move(self.color, self.offsets, board)

        return valid_moves

    def __str__(self):
        """
        Returns a string representation of the knight.
        """
        if self.color == "w":
            return "♘"
        else:
            return "♞"
    def __repr__(self) -> str:
        return self.color + 'n'

def main():
    pass

if __name__ == "__main__":
    main()
