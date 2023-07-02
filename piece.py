from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, color, row, col):
        self.col = col
        self.row = row
        self.color = color
        self.has_moved = False


    @abstractmethod
    def get_moves(self, board, row, col):
        """
        Returns a list of valid moves for the piece at the given row and column
        on the given board.
        """
        pass

    def update_pos(self, r, c):
        self.col = c
        self.row = r


    def __str__(self):
        """
        Returns a string representation of the piece.
        """
        pass
