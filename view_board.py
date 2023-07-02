from constants import WHITE, BLACK
import pygame
from piece import ChessPiece
class ViewBoard():
    rect = (0, 0, 800, 800)

    def __init__(self) -> None:
        pass
    def draw_board(self, win):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(win, color, pygame.Rect(i * 100, j * 100, 100, 100))

    def draw_pieces(self, board, win):
        col_offset = -100 
        for r in board:
            row_offset = 0
            col_offset += 100
            for piece in r:
                if isinstance(piece, ChessPiece) :
                    img = pygame.transform.scale(piece.img, (55,55) )
                    win.blit(img, pygame.Rect(20 + row_offset, 20 + col_offset , 55, 55))

                row_offset += 100
    def highlight_valid_moves(self,win,  moves, cap):
        if moves == None:
            pass

        else:

            sur = pygame.Surface((100, 100))
            sur.set_alpha(100)
            sur.fill(pygame.Color("green"))
            for (r, c) in moves:
                if (r, c) not in cap:
                    win.blit(sur,( c * 100, r * 100 ))
    
    def highlight_pos(self, win, r,c):
        if r == None and c == None:
            pass
        else:
            sur = pygame.Surface((100, 100))
            sur.set_alpha(100)
            sur.fill(pygame.Color("blue"))
            win.blit(sur,( c * 100, r * 100 ))
    def highlight_capturing(self, win, cap): 
            if len(cap) == 0:
                pass
            else:

                for (r, c) in cap:
                    sur = pygame.Surface((100, 100))
                    sur.set_alpha(100)
                    sur.fill(pygame.Color("red"))
                    win.blit(sur,( c * 100, r * 100 ))




            



def main():
    pass

if __name__ == "__main__":
    main()