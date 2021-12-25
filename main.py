from _2048.game import Game
from settings import *

if __name__ == '__main__':
    game = Game(SIZE, WIN_VALUE)
    game.start()
