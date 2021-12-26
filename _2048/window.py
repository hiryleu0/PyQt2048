import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from .constants import *


class Window:
    def __init__(self, size):
        self.app = QApplication(sys.argv)
        self.widget = QWidget()
        self.message_box = QMessageBox()

        self.menu = QMenuBar(self.widget)
        self.menu.setFixedHeight(MENU_HEIGHT)

        widget_width = size * BUTTON_SIZE + (size + 1) * BUTTON_MARGIN
        widget_height = widget_width + MENU_HEIGHT
        self.widget.setFixedSize(widget_width, widget_height)

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
        self.widget.setWindowTitle("PyGt5 2048")

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
