from king import King
from queen import Queen
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from piece import ChessPiece


class Board:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.is_selected = False
        self.initialize_board()

    def initialize_board(self):
        self.initialize_black_pieces()
        self.initialize_white_pieces()
        self.initialize_pawns()

    def initialize_black_pieces(self):
        self.board[7][0] = Rook('b', 7, 0)
        self.board[7][1] = Knight('b', 7, 1)
        self.board[7][2] = Bishop('b', 7, 2)
        self.board[7][3] = Queen('b', 7, 3)
        self.board[7][4] = King('b', 7, 4)
        self.board[7][5] = Bishop('b', 7, 5)
        self.board[7][6] = Knight('b', 7, 6)
        self.board[7][7] = Rook('b', 7, 7)

    def initialize_white_pieces(self):
        self.board[0][0] = Rook('w', 0, 0)
        self.board[0][1] = Knight('w', 0, 1)
        self.board[0][2] = Bishop('w', 0, 2)
        self.board[0][3] = Queen('w', 0, 3)
        self.board[0][4] = King('w', 0, 4)
        self.board[0][5] = Bishop('w', 0, 5)
        self.board[0][6] = Knight('w', 0, 6)
        self.board[0][7] = Rook('w', 0, 7)

    def initialize_pawns(self):
        for c in range(8):
            self.board[1][c] = Pawn('w', 1, c)
            self.board[6][c] = Pawn('b', 6, c)

    def select(self, r, c):
        piece = self.board[r][c] if self.is_within_bounds(r, c) else None
        self.is_selected = piece is not None
        return piece

    def move(self, r_old, c_old, r_new, c_new):
        piece = self.select(r_old, c_old)
        valid_moves = self.get_piece_moves(r_old, c_old)
        if (r_new, c_new) in valid_moves:
            self.board[r_new][c_new] = piece
            self.board[r_old][c_old] = None
            piece.update_pos(r_new, c_new)
            piece.has_moved = True
            self.pawn_promotion(r_new, c_new)
            return True
        else:
            return False

    def get_piece_moves(self, r, c):
        piece = self.select(r, c)
        if piece is None:
            return []
        return piece.get_moves(self.board)

    def can_capture(self, r, c):
        piece = self.select(r, c)
        if piece is None:
            return []
        valid_moves = self.get_piece_moves(r, c)
        return [(r, c) for r, c in valid_moves if isinstance(self.board[r][c], ChessPiece)]

    def pawn_promotion(self, r, c):
        piece = self.select(r, c)
        if isinstance(piece, Pawn) and piece.color == 'w' and r == 7:
            self.board[r][c] = Queen('w', r, c)

    def is_within_bounds(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def find_king_position(self, color):
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if isinstance(piece, King) and piece.color == color:
                    return r, c
        return None

    def is_king_in_check(self, color):
        king_pos = self.find_king_position(color)
        if king_pos is None:
            return False

        opponent_color = 'b' if color == 'w' else 'w'
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if isinstance(piece, ChessPiece) and piece.color == opponent_color:
                    valid_moves = piece.get_moves(self.board)
                    if king_pos in valid_moves:
                        return True
        return False

    def is_checkmate(self, color):
        if not self.is_king_in_check(color):
            return False

        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if isinstance(piece, ChessPiece) and piece.color == color:
                    valid_moves = self.get_piece_moves(r, c)
                    for move in valid_moves:
                        r_new, c_new = move
                        if self.simulate_move(r, c, r_new, c_new):
                            return False
        return True

    def is_stalemate(self, color):
        if self.is_king_in_check(color):
            return False

        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if isinstance(piece, ChessPiece) and piece.color == color:
                    valid_moves = self.get_piece_moves(r, c)
                    for move in valid_moves:
                        r_new, c_new = move
                        if self.simulate_move(r, c, r_new, c_new):
                            return False
        return True

    def simulate_move(self, r_old, c_old, r_new, c_new):
        piece = self.select(r_old, c_old)
        piece_old = self.board[r_old][c_old]
        piece_new = self.board[r_new][c_new]
        self.board[r_new][c_new] = piece
        self.board[r_old][c_old] = None
        piece.update_pos(r_new, c_new)

        is_checkmate = self.is_king_in_check(piece.color)

        self.board[r_old][c_old] = piece_old
        self.board[r_new][c_new] = piece_new
        piece.update_pos(r_old, c_old)

        return is_checkmate


def main():
    pass


if __name__ == "__main__":
    main()
