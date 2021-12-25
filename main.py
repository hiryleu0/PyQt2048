import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import shuffle

from constants import *

LabelGrid = list[list[QLabel]]
labels: LabelGrid = []


def generate_new_two():
    xs = [x for x in range(BUTTONS_IN_ROW)]
    ys = [y for y in range(BUTTONS_IN_ROW)]
    shuffle(xs)
    shuffle(ys)

    for x in xs:
        for y in ys:
            label = labels[x][y]
            if label.text() == '0':
                update_label(label, 2)
                return


def update_label(label: QLabel, value: int):
    label.setText(str(value))
    label.setStyleSheet('background-color: ' + COLOR[value] + ';'
                                                              'border: 2px solid black;'
                                                              'border-radius: 5px;')
    label.repaint()


def key_press_event(event: QKeyEvent):
    if event.key() == Qt.Key.Key_W:
        label = labels[0][0]
        value = int(label.text())
        new_value = 1 if value == 0 else value * 2
        update_label(label, new_value)

    elif event.key() == Qt.Key.Key_S:
        print('S')
    elif event.key() == Qt.Key.Key_A:
        print('A')
    elif event.key() == Qt.Key.Key_D:
        print('D')

    generate_new_two()


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget_size = BUTTONS_IN_ROW * BUTTON_SIZE + (BUTTONS_IN_ROW + 1) * BUTTON_MARGIN
    widget.setFixedSize(widget_size, widget_size)
    widget.keyPressEvent = key_press_event

    shift = BUTTON_MARGIN + BUTTON_SIZE
    for i in range(BUTTONS_IN_ROW):
        labels_row = []
        for j in range(BUTTONS_IN_ROW):
            label = QLabel(widget)
            label.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)

            x_shift = BUTTON_MARGIN + i * shift
            y_shift = BUTTON_MARGIN + j * shift
            label.move(x_shift, y_shift)
            label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            label.setAlignment(Qt.AlignCenter)
            label.setText('0')
            label.setStyleSheet('background-color: ' + COLOR[0] + ';'
                                                                  'border: 2px solid black;'
                                                                  'border-radius: 5px;')
            labels_row.append(label)
        labels.append(labels_row)

    generate_new_two()
    widget.move(50, 50)
    widget.setWindowTitle("PyGt5 2048")
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
