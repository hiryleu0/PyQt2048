import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from .constants import *


class Window:
    def __init_icon__(self):
        self.icon = QIcon()
        self.icon.addFile('_2048/icons/icon-16.png', QSize(16, 16))
        self.icon.addFile('_2048/icons/icon-24.png', QSize(24, 24))
        self.icon.addFile('_2048/icons/icon-32.png', QSize(32, 32))
        self.icon.addFile('_2048/icons/icon-48.png', QSize(48, 48))
        self.icon.addFile('_2048/icons/icon-256.png', QSize(256, 256))
        self.app.setWindowIcon(self.icon)

    def __init_menu__(self):
        self.menu = QMenuBar(self.widget)
        self.menu.setFixedHeight(MENU_HEIGHT)
        self.menu.setStyleSheet('background-color: #EEE;')

    def __init_widget(self, size):
        widget_width = size * BUTTON_SIZE + (size + 1) * BUTTON_MARGIN
        widget_height = widget_width + MENU_HEIGHT
        self.widget.setFixedSize(widget_width, widget_height)

    def __init_labels__(self, size):
        shift = BUTTON_MARGIN + BUTTON_SIZE
        self.labels = []
        for i in range(size):
            labels_row = []
            for j in range(size):
                label = QLabel(self.widget)
                label.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)

                x_shift = BUTTON_MARGIN + j * shift
                y_shift = MENU_HEIGHT + BUTTON_MARGIN + i * shift
                label.move(x_shift, y_shift)
                label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                label.setAlignment(Qt.AlignCenter)
                label.setText('')
                label.setStyleSheet('background-color: ' + COLOR[0] + ';'
                                                                      'border: 2px solid black;'
                                                                      'border-radius: 5px;'
                                                                      'font-size: 20px;')
                labels_row.append(label)
            self.labels.append(labels_row)

    def __init__(self, size):
        self.app = QApplication(sys.argv)
        self.widget = QWidget()
        self.widget.setWindowTitle("PyGt5 2048")

        self.__init_icon__()
        self.__init_menu__()
        self.__init_widget(size)
        self.__init_labels__(size)

    def update_label(self, x, y, value):
        label = self.labels[x][y]
        label.setText(str(value if value > 0 else ''))
        label.setStyleSheet('background-color: ' + COLOR[value] + ';'
                                                                  'border: 2px solid black;'
                                                                  'border-radius: 5px;'
                                                                  'font-size: 20px;')
        label.repaint()

    def show(self, x, y):
        self.widget.move(x, y)
        self.widget.show()
        self.app.exec_()

    def win(self):
        result = QMessageBox.question(self.widget, "Success!", "Wanna play again?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        return result == QMessageBox.Yes

    def lose(self):
        result = QMessageBox.critical(self.widget, "Failure!", "Wanna play again?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        return result == QMessageBox.Yes
