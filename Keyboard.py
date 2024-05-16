import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
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
        self.gridLayout.setSpacing(0)  # Уменьшение расстояния между кнопками
        self.gridLayout.setContentsMargins(0, 0, 0, 0)  # Уменьшение отступов до минимума

        self.keys = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '←'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
            ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Space']
        ]

        # Настройка размеров для каждой кнопки
        self.key_sizes = {
            '←': (80, 40),
            'Tab': (80, 40),
            'Caps': (80, 40),
            'Enter': (80, 40),
            'Shift': (120, 40),
            'Space': (200, 40),
            '`': (60, 40),
        }

        self.buttons = [] # списко для хранения кнопок
        # Добавление кнопок в сетку
        for row, key_row in enumerate(self.keys):
            col_offset = 0
            row_buttons = []
            for col, key in enumerate(key_row):
                button = QPushButton(key)
                width, height = self.key_sizes.get(key, (40, 40))  # Развернем кортеж
                button.setFixedSize(width, height)
                if (key != 'Space'):
                    row_buttons.append(button)
                if key in ['`']:
                    self.gridLayout.addWidget(button, row, col + col_offset)
                elif key in ['←', 'Enter', 'Shift']:
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
                # button.pressed.connect(lambda _, k=key: self.key_pressed(k))  # Подключаем сигнал clicked
                # row_buttons.append(button)
            self.buttons.append(row_buttons)
         

        space_button = QPushButton('Space')
        space_button.setFixedSize(200, 40)
        self.gridLayout.addWidget(space_button, 4, 4, 1, 14)
        self.buttons[4].append(space_button)

        max_length = max(len(row) for row in self.buttons)
        for col in range(max_length):
            for row in range(len(self.buttons)):
                if col < len(self.buttons[row]):
                    self.buttons[row][col].setStyleSheet(self.get_button_style(self.keys[row][col], col))


    # def keyPressEvent(self, event):
    #     key = event.key()
    #     print(key)
       
    def get_button_style(self, key, col):
        base_style = """
            QPushButton {
                border-radius: 4px;
                font-size: 16px;
                font-weight: 700;

            }
            QPushButton:pressed {
                background-color: #dcdcdc;
            }
        """
        if key in ['←', 'Tab', 'Caps', 'Enter', 'Shift', 'Space']:
            special_style = """
                QPushButton {
                    background-color: rgb(219,226,229);
                    font-weight: bold;
                }
                QPushButton:pressed {
                    background-color: #a0a0a0;
                }
            """
            return base_style + special_style
        if (col % 2 == 0):
            even_style = """
            QPushButton {
                background-color: rgb(201,200,255);
                color: rgb(44, 43, 107);
            }
            QPushButton:pressed {
                background-color: #dcdcdc;
            }
        """ 
            return base_style + even_style 
        else:
            odd_style = """
            QPushButton {
                background-color: rgb(172, 243, 199);
                color: rgb(23, 113, 58);
            }
            QPushButton:pressed {
                background-color: #dcdcdc;
            }
        """ 
            return base_style + odd_style
        return base_style
    def key_pressed(self, key):
        print(f'Key {key} pressed')
