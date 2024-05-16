import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import QSize

class Keyboard(QWidget):
    def __init__(self): 
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        layout.addLayout(self.gridLayout)
        self.setLayout(layout)

        # Настройка отступов и расстояния между виджетами
        self.gridLayout.setSpacing(1)  # Уменьшение расстояния между кнопками
        self.gridLayout.setContentsMargins(1, 1, 1, 1)  # Уменьшение отступов до минимума

        self.keys = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
            ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Space']
        ]

        # Настройка размеров для каждой кнопки
        self.key_sizes = {
            'Backspace': (90, 40),
            'Tab': (60, 40),
            'Caps': (60, 40),
            'Enter': (80, 40),
            'Shift': (80, 40),
            'Space': (200, 40),
        }

        # Добавление кнопок в сетку
        for row, key_row in enumerate(self.keys):
            col_offset = 0
            for col, key in enumerate(key_row):
                button = QPushButton(key)
                width, height = self.key_sizes.get(key, (40, 40))  # Развернем кортеж
                button.setFixedSize(width, height)
                if key in ['Backspace', 'Enter', 'Shift']:
                    if key == 'Shift' and row == 3:
                        self.gridLayout.addWidget(button, row, col + col_offset, 1, 2)
                        col_offset += 1
                    else:
                        self.gridLayout.addWidget(button, row, col + col_offset, 1, 2)
                        col_offset += 1
                elif (key == 'Space'):
                    pass
                else:
                    self.gridLayout.addWidget(button, row, col + col_offset)
                button.clicked.connect(lambda _, k=key: self.key_pressed(k))  # Подключаем сигнал clicked

        space_button = QPushButton('Space')
        space_button.setFixedSize(200, 40)
        self.gridLayout.addWidget(space_button, 4, 4, 1, 14)


    def key_pressed(self, key):
        print(f'Key {key} pressed')

