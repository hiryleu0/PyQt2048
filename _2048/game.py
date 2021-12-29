from enum import Enum

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .window import Window
from .board import Board
from .constants import *


class GameState(Enum):
    STARTED = 1
    WON = 2
    LOST = 3


class Game:
    def __init_game_menu_actions__(self):
        game_menu = self.window.menu.addMenu("Game")
        new_game_action = game_menu.addAction("New game")
        new_game_action.setShortcut("F2")
        new_game_action.triggered.connect(self.generate_new_game_handler())
        exit_action = game_menu.addAction("Exit")
        exit_action.setShortcut("Alt+F4")
        exit_action.triggered.connect(self.generate_exit_game_handler())

    def __init_settings_menu_actions__(self):
        settings_menu = self.window.menu.addMenu("Settings")
        win_value_menu = settings_menu.addMenu("Win value")
        value = 2
        for i in range(2, 12):
            value = value * 2
            size_action: QAction = win_value_menu.addAction(str(value))
            size_action.setCheckable(True)
            if value == WIN_VALUE:
                size_action.setChecked(True)
                self.checked_win_value_action = size_action
            size_action.triggered.connect(self.generate_win_value_change_handler(value, size_action))

    def __init_about_menu_actions(self):
        about_action = self.window.menu.addAction("About")
        about_action.setShortcut("Ctrl+H")
        about_action.triggered.connect(self.generate_about_handler())

    def __init_menu_actions__(self):
        self.__init_game_menu_actions__()
        self.__init_settings_menu_actions__()
        self.__init_about_menu_actions()

    def __init__(self):
        self.win_value = WIN_VALUE
        self.state = GameState.STARTED

        self.window = Window(SIZE)
        self.__init_menu_actions__()

        self.board = Board(SIZE)
        x, y = self.board.generate_random_two()
        self.window.update_label(x, y, 2, True)

        self.window.widget.keyPressEvent = self.generate_key_press_handler()

    def start_again(self):
        self.state = GameState.STARTED
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.window.update_label(i, j, 0, False)
        self.board = Board(self.board.size)
        x, y = self.board.generate_random_two()
        self.window.update_label(x, y, 2, True)

    def generate_key_press_handler(self):
        def key_press_handler(event: QKeyEvent):
            if self.state != GameState.STARTED:
                return

            key = event.key()
            if key == 87:
                moved, moved_board = self.board.make_move(0)
            elif key == 65:
                moved, moved_board = self.board.make_move(1)
            elif key == 83:
                moved, moved_board = self.board.make_move(2)
            elif key == 68:
                moved, moved_board = self.board.make_move(3)
            else:
                return

            if not moved:
                return

            x, y = self.board.generate_random_two()
            moved_board[x][y] = True
            for i in range(self.board.size):
                for j in range(self.board.size):
                    self.window.update_label(i, j, self.board.board[i][j], moved_board[i][j])

            if self.board.is_won(self.win_value):
                self.state = GameState.WON
                if self.window.win():
                    self.start_again()
            elif self.board.is_lost():
                self.state = GameState.LOST
                if self.window.lose():
                    self.start_again()

        return key_press_handler

    def generate_new_game_handler(self):
        def new_game_handler(_):
            result = QMessageBox.question(self.window.widget, "New game", "Are you sure?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.start_again()
        return new_game_handler

    def generate_exit_game_handler(self):
        def exit_game_handler(_):
            result = QMessageBox.question(self.window.widget, "Exit game", "Are you sure?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.window.app.exit(0)
        return exit_game_handler

    def generate_win_value_change_handler(self, value, action):
        def win_value_change_handler(_):
            self.win_value = value
            self.checked_win_value_action.setChecked(False)
            self.checked_win_value_action = action
            action.setChecked(True)
            result = self.board.is_won(value)
            if result:
                if self.window.win():
                    self.start_again()
            else:
                self.state = GameState.STARTED
        return win_value_change_handler

    def generate_about_handler(self):
        def about_handler(_):
            QMessageBox.about(self.window.widget, "About", "Simple 2048 powered by PyQt5")
        return about_handler

    def start(self):
        self.window.show(100, 100)




