# This is our driver file. Responsible for handling user input and displaying the current gameState object.

import pygame as p

from chessengine import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT / DIMENSION

MAX_FPS = 15
IMAGES = {}

# Initialize a global dictionary of imgaes.


def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(
            p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE)
        )
        # we can access an Image by saying 'IMAGES['wp']'


def main():
    p.init()

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    gs = ChessEngine.GameState()
    loadImages()
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)       # draw squares on the board
    drawPieces(screen, gs.board)    # draw pieces on top of those squares


def drawBoard(screen): 


def drawPieces(screen, board):



if __name__ == "__main__":
    main()
