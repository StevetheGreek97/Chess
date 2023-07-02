from piece import ChessPiece
import numpy as np
import pygame
from moves import Moves
BOARD = np.zeros((8, 8))

class King(ChessPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        if self.color == 'w':
            img_path = 'images/white_k.png'
            self.img = pygame.image.load(img_path)
        else:
            
            img_path = 'images/black_k.png'
            self.img = pygame.image.load(img_path)

    def get_moves(self, board):
        """
        Returns a list of valid moves for the king at the given row and column
        on the given board.
        """
        valid_moves = Moves(self.row, self.col).king_step(board)

        return valid_moves

    def __str__(self):
        """
        Returns a string representation of the king.
        """
        if self.color == "w":
            return "♔"
        else:
            return "♚"

    def __repr__(self) -> str:
        return self.color + 'k'
        
def show_moves(moves):
    for row, col in moves:
        BOARD[row][col] = 2

def main():
    king = King('w', 5,0)
    # print(BOARD)
    king.update_pos(5, 5)

    print(king.get_moves())
    show_moves(king.get_moves())
    print(king)
    print(BOARD)

if __name__ == "__main__":
    main()

