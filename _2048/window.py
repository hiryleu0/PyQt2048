import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from .constants import *


class Window:
    def __init__(self, size):
        self.app = QApplication(sys.argv)
        self.widget = QWidget()
        widget_size = size * BUTTON_SIZE + (size + 1) * BUTTON_MARGIN
        self.widget.setFixedSize(widget_size, widget_size)

        shift = BUTTON_MARGIN + BUTTON_SIZE
        self.labels = []
        for i in range(size):
            labels_row = []
            for j in range(size):
                label = QLabel(self.widget)
                label.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)

                x_shift = BUTTON_MARGIN + j * shift
                y_shift = BUTTON_MARGIN + i * shift
                label.move(x_shift, y_shift)
                label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                label.setAlignment(Qt.AlignCenter)
                label.setText('')
                label.setStyleSheet('background-color: ' + COLOR[0] + ';'
                                                                      'border: 2px solid black;'
                                                                      'border-radius: 5px;')
                labels_row.append(label)
            self.labels.append(labels_row)
        self.widget.setWindowTitle("PyGt5 2048")

    def update_label(self, x, y, value):
        label = self.labels[x][y]
        label.setText(str(value if value > 0 else ''))
        label.setStyleSheet('background-color: ' + COLOR[value] + ';'
                                                                  'border: 2px solid black;'
                                                                  'border-radius: 5px;')
        label.repaint()

    def show(self, x, y):
        self.widget.move(x, y)
        self.widget.show()
        self.app.exec_()

    def win(self):
        print('WON!')

    def lose(self):
        print('LOST!')
