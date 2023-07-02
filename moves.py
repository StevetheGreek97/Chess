
class Moves:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
    

    def knights_move(self,color, offsets, BOARD):
        valid_moves = []
        # Loop over the possible moves
        for offset in offsets:
            new_row, new_col = self.row + offset[0], self.col + offset[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if BOARD[new_row][new_col] == 0:
                    valid_moves.append((new_row, new_col))
                elif BOARD[new_row][new_col] != 0 and BOARD[new_row][new_col].color != color:
                    valid_moves.append((new_row, new_col))
                    
        return valid_moves
    
    def diagonal(self,color, board):
        # List to hold valid moves
        valid_moves = []

        # Define possible directions (horizontal and vertical)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        # Loop through all possible directions
        for dr, dc in directions:
            # Starting position for this direction
            r, c = self.row + dr, self.col + dc

            # Keep moving in this direction until we reach the edge of the board or an obstruction
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 0:
                    valid_moves.append((r, c))
                elif board[r][c] != 0 and board[r][c].color != color:
                    valid_moves.append((r, c))
                    break
                else:
                    break

                # Move to the next square in this direction
                r += dr
                c += dc

        return valid_moves
    def horizontal_vertical(self,color, board):


        # List to hold valid moves
        valid_moves = []

        # Define possible directions (horizontal and vertical)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Loop through all possible directions
        for dr, dc in directions:
            # Starting position for this direction
            r, c = self.row + dr, self.col + dc

            # Keep moving in this direction until we reach the edge of the board or an obstruction
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 0:
                    valid_moves.append((r, c))
                elif board[r][c] != 0 and board[r][c].color != color:
                    valid_moves.append((r, c))
                    break
                else:
                    break

                # Move to the next square in this direction
                r += dr
                c += dc

        return valid_moves

    
    def king_step(self, board):
        valid_moves = []

        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                r, c = self.row + dr, self.col + dc
                if (r < 0 or r >= 8 or c < 0 or c >= 8):
                    continue
                if board[r][c] == 0:
                    valid_moves.append((r, c))
        return valid_moves
    def pawn_move(self, color, BOARD):
        valid_moves = []
        
        # Compute the row and column offsets for pawn moves.
        if color == "w":
            row_offset = 1
            starting_row = 1
            promotion_row = 7
        else:
            row_offset = -1
            starting_row = 6
            promotion_row = 0
        
        # Check if the pawn can move one square forward.
        new_row, new_col = self.row + row_offset, self.col
        if 0 <= new_row < 8 and 0 <= new_col < 8 and BOARD[new_row][new_col] == 0:
            valid_moves.append((new_row, new_col))
            
            # If the pawn is on its starting row, it can move two squares forward.
            if self.row == starting_row:
                new_row, new_col = self.row + 2 * row_offset, self.col
                if BOARD[new_row][new_col] == 0:
                    valid_moves.append((new_row, new_col))
        
        # Check if the pawn can capture diagonally.
        for col_offset in (-1, 1):
            new_row, new_col = self.row + row_offset, self.col + col_offset
            if 0 <= new_row < 8 and 0 <= new_col < 8 and BOARD[new_row][new_col] != 0 and BOARD[new_row][new_col].color != color:
                valid_moves.append((new_row, new_col))


        
            

                

        return valid_moves
    def castle_kingside(self):
        pass
    def castle_queenside(self):
        pass
    def en_passant(self):
        pass
