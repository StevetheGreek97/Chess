import pygame
from booard import Board
from view_board import ViewBoard
from king import King
# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = HEIGHT = 800  # width and height of the chess board
DIMENSION = 8  # the dimensions of the chess board
SQ_SIZE = HEIGHT // DIMENSION  # the size of each of the squares in the board
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Chess Game")

# Create objects
board = Board()
view = ViewBoard()
current_player = "w"

def click(pos):
    """
    Returns the position (x, y) in the range 0-7 0-7.
    """
    rect = (0, 0, 800, 800)
    x, y = pos[0], pos[1]
    if rect[0] < x < rect[0] + rect[2] and rect[1] < y < rect[1] + rect[3]:
        divX = x - rect[0]
        divY = y - rect[1]
        i = int(divX / (rect[2] / 8))
        j = int(divY / (rect[3] / 8))
        return j, i

    return -1, -1

def change_turn():
    """
    Changes the current player's turn.
    """
    global current_player
    if current_player == "w":
        current_player = "b"
    else:
        current_player = "w"

def is_turn(r, c):
    """
    Checks if it is the current player's turn to move.
    """
    piece = board.select(r, c)
    if piece is None:
        return True
    elif piece.color == current_player:
        return True
    elif selected_pos is not None:
        return True
    else:
        return False

def is_game_over():
    """
    Checks if the game is over (checkmate or stalemate).
    """
    if board.is_checkmate(current_player):
        print(f"Checkmate! {current_player} has won!")
        return True
    elif board.is_stalemate(current_player):
        print("Stalemate!")
        return True
    else:
        return False

# Main game loop
clock = pygame.time.Clock()
running = True
selected_pos = None

while running:
    # Limit the frame rate
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    r, c = click(pos)

                    if is_turn(r, c):
                        if selected_pos is None:
                            piece = board.select(r, c)

                            if piece is not None:
                                selected_pos = (r, c)
                                valid_moves_selected_p = board.get_piece_moves(r, c)
                        else:
                            flag = board.move(*selected_pos, r, c)

                            if flag:
                                change_turn()

                            selected_pos = None
                            valid_moves_selected_p = None
    # Draw the board and pieces
    view.draw_board(screen)
    view.draw_pieces(board.board, screen)

    # Highlight the selected piece and valid moves
    if selected_pos is not None:
        view.highlight_pos(screen, *selected_pos)
        cap = board.can_capture(*selected_pos)
        # print(cap)
        view.highlight_valid_moves(screen, valid_moves_selected_p, cap)
        view.highlight_capturing(screen, cap)

    # if is_game_over():
    #     running = False

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
