import pygame
import sys
from board import MonopolyBoard
from utils import draw_text
from property import Property

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Monopoly Game")

# Colors
LIGHT_GREEN = (240, 255, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_COLOUR = LIGHT_GREEN

# Sizes and positions
SQ_SIZE = 160
RECT_SIZE = 160
BORDER = 4
SQ_INITIAL_POS = (300, 0)
END_POS = (SQ_INITIAL_POS[0] + 840, SQ_INITIAL_POS[1] + 840)
VRECT_INITIAL_POS = (SQ_INITIAL_POS[0] - BORDER + SQ_SIZE, 0)
HRECT_INITIAL_POS = (0, SQ_INITIAL_POS[1] - BORDER + SQ_SIZE)


# Create the game board
board = MonopolyBoard()
board.add_all_spaces()

def draw_sq(surface, color, position, size, border=BORDER):
    pygame.draw.rect(surface, color, (*position, size, size))
    pygame.draw.rect(surface, BLACK, (*position, size, size), border)  # Border


def draw_vrect(surface, color, position, size, border=BORDER):
    pygame.draw.rect(surface, color, (*position, size // 2, size))
    pygame.draw.rect(surface, BLACK, (*position, size // 2, size), border)  # Border


def draw_hrect(surface, color, position, size, border=4):
    pygame.draw.rect(surface, color, (*position, size, size // 2))
    pygame.draw.rect(surface, BLACK, (*position, size, size // 2), border)  # Border


def draw_board(surface):
    # Draw corners
    draw_sq(surface, BG_COLOUR, SQ_INITIAL_POS, SQ_SIZE, BORDER)
    draw_sq(surface, BG_COLOUR, (END_POS[0], SQ_INITIAL_POS[1]), SQ_SIZE, BORDER)
    draw_sq(surface, BG_COLOUR, (SQ_INITIAL_POS[0], END_POS[1]), SQ_SIZE, BORDER)
    draw_sq(surface, BG_COLOUR, (END_POS[0], END_POS[1]), SQ_SIZE, BORDER)
    
    # Draw the top row
    for i in range(9):
        draw_vrect(surface, BG_COLOUR, (VRECT_INITIAL_POS[0] + ((RECT_SIZE - 2 * BORDER) // 2 * i), VRECT_INITIAL_POS[1]), RECT_SIZE, BORDER)
    
    # Draw the bottom row
    for i in range(9):
        draw_vrect(surface, BG_COLOUR, (VRECT_INITIAL_POS[0] + ((RECT_SIZE - 2 * BORDER) // 2 * i), END_POS[1]), RECT_SIZE, BORDER)

    # Draw the left column
    for i in range(9):
        draw_hrect(surface, BG_COLOUR, (SQ_INITIAL_POS[0], HRECT_INITIAL_POS[1] + ((RECT_SIZE - 2 * BORDER) // 2 * i)), RECT_SIZE, BORDER)

    # Draw the right column
    for i in range(9):
        draw_hrect(surface, BG_COLOUR, (END_POS[0], HRECT_INITIAL_POS[1] + ((RECT_SIZE - 2 * BORDER) // 2 * i)), RECT_SIZE, BORDER)


# Main game loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background
        screen.fill(WHITE)

        # Draw the board
        draw_board(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()