from enum import Enum

from PyQt5.QtGui import *

from .window import Window
from .board import Board


class GameState(Enum):
    STARTED = 1
    WON = 2
    LOST = 3


class Game:
    def __init__(self, size, win_value):
        self.win_value = win_value
        self.state = GameState.STARTED
        self.window = Window(size)
        self.board = Board(size)
        x, y = self.board.generate_random_two()
        self.window.update_label(x, y, 2)
        self.window.widget.keyPressEvent = self.generate_key_press_handler()

    def start_again(self):
        self.state = GameState.STARTED
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.window.update_label(i, j, 0)
        self.board = Board(self.board.size)
        x, y = self.board.generate_random_two()
        self.window.update_label(x, y, 2)

    def generate_key_press_handler(self):
        def key_press_handler(event: QKeyEvent):
            if self.state != GameState.STARTED:
                return

            key = event.key()
            moved = False
            if key == 87:
                moved = self.board.make_move(0)
            elif key == 65:
                moved = self.board.make_move(1)
            elif key == 83:
                moved = self.board.make_move(2)
            elif key == 68:
                moved = self.board.make_move(3)

            if moved:
                self.board.generate_random_two()
                for i in range(self.board.size):
                    for j in range(self.board.size):
                        self.window.update_label(i, j, self.board.board[i][j])

            if self.board.is_lost():
                self.state = GameState.LOST
                if self.window.lose():
                    self.start_again()
            elif self.board.is_won(self.win_value):
                self.state = GameState.WON
                if self.window.win():
                    self.start_again()

        return key_press_handler

    def start(self):
        self.window.show(100, 100)




