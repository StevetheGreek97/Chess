from king import King
from queen import Queen
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from piece import ChessPiece
import pygame
class Board():
    def __init__(self) -> None:
        self.board = [[0 for x in range(8)] for _ in range(8)]

        self.board[7][0] = Rook(  'b', 7, 0)
        self.board[7][1] = Knight('b', 7, 1)
        self.board[7][2] = Bishop('b', 7, 2)
        self.board[7][3] = Queen( 'b', 7, 3)
        self.board[7][4] = King(  'b', 7, 4)
        self.board[7][5] = Bishop('b', 7, 5)
        self.board[7][6] = Knight('b', 7, 6)
        self.board[7][7] = Rook(  'b', 7, 7)

        
        self.board[0][0] = Rook(  'w', 0, 0)
        self.board[0][1] = Knight('w', 0, 1)
        self.board[0][2] = Bishop('w', 0, 2)
        self.board[0][3] = Queen( 'w', 0, 3)
        self.board[0][4] = King(  'w', 0, 4)
        self.board[0][5] = Bishop('w', 0, 5)
        self.board[0][6] = Knight('w', 0, 6)
        self.board[0][7] = Rook(  'w', 0, 7)


        for c in range(8):
            self.board[1][c] = Pawn('w', 1, c)
            self.board[6][c] = Pawn('b', 6,  c)

        self.is_selected = False
        
        


    def get_piece_moves(self,r, c):
        piece = self.select(r, c)
        if piece != None:
            valid_moves = piece.get_moves(self.board)
        else:
            return []

        return valid_moves

    def select(self, r, c):
        if r == None and c == None:
            return None
        else:
            piece = self.board[r][c]
            
            
            if piece != 0:
                self.is_selected = True
                return piece
            else:
                self.is_selected = False
                return None
        
    def _update_board(self, r_old, c_old, r_new, c_new, piece):
        self.board[r_old][c_old] = 0
        self.board[r_new][c_new] = piece 


    def move(self, r_old, c_old, r_new, c_new):
        piece = self.select(r_old, c_old)
        valid_moves = self.get_piece_moves(r_old, c_old)
        if (r_new, c_new) in valid_moves:
            piece.update_pos( r_new, c_new)
            self._update_board( r_old, c_old, r_new, c_new, piece)
            piece.has_moved = True
            self.pawn_promotion(r_new, c_new)
            return True
        else:
            return False
            # print('invalid move')
            
    def can_capture(self, r, c):
        valid_capture = []
        valid_moves = self.get_piece_moves(r, c)
        for (r,c) in valid_moves:
            if isinstance(self.board[r][c], ChessPiece):
                valid_capture.append((r, c))
        return valid_capture

    def pawn_promotion(self, r, c):
        piece = self.select(r, c)
        if isinstance(piece, Pawn):
            if piece.color == 'w' and r == 7:

                self.board[r][c] = Queen( 'w', r, c)

    def is_king_in_check(self, color):
        king = None
        for row in self.board:
            for piece in row:
                if isinstance(piece, King) and piece.color == color:
                    king = piece
                    break

        if king is None:
            return False

        king_pos = king.row, king.col
        if color == 'w':
            opponent_color = 'b' 
        else:
            opponent_color = 'w' 


        for row in self.board:
            for piece in row:
                if isinstance(piece, ChessPiece) and piece.color == opponent_color:
                    valid_moves = piece.get_moves(self.board)
                    if king_pos in valid_moves:
                        return True

        return False









def main():
    pass


if __name__ == "__main__":
    main()

