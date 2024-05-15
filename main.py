import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout

class Keyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        gridLayout = QGridLayout()
        layout.addLayout(gridLayout)
        self.setLayout(layout)

        # Настройка отступов и расстояния между виджетами
        gridLayout.setSpacing(1)  # Уменьшение расстояния между кнопками
        gridLayout.setContentsMargins(1, 1, 1, 1)  # Уменьшение отступов до минимума

        keys = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
            ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Space']
        ]

        # Настройка размеров для каждой кнопки
        key_sizes = {
            'Backspace': (80, 40),
            'Tab': (60, 40),
            'Caps': (60, 40),
            'Enter': (80, 40),
            'Shift': (80, 40),
            'Space': (200, 40),
        }

        # Добавление кнопок в сетку
        for row, key_row in enumerate(keys):
            col_offset = 0
            for col, key in enumerate(key_row):
                button = QPushButton(key)
                width, height = key_sizes.get(key, (40, 40))  # Развернем кортеж
                button.setFixedSize(width, height)
                if key in ['Backspace', 'Enter', 'Shift']:
                    if key == 'Shift' and row == 3:
                        gridLayout.addWidget(button, row, col + col_offset, 1, 2)
                        col_offset += 1
                    else:
                        gridLayout.addWidget(button, row, col + col_offset, 1, 2)
                        col_offset += 1
                elif (key == 'Space'):
                    pass
                else:
                    gridLayout.addWidget(button, row, col + col_offset)
        space_button = QPushButton('Space')
        space_button.setFixedSize(200, 40)
        gridLayout.addWidget(space_button, 4, 4, 1, 14)

        self.setWindowTitle('QWERTY Keyboard')
        self.resize(800, 300)  # Настройка размера окна
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Keyboard()
    sys.exit(app.exec_())
