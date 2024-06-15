import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, QTimer

class Keyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Главный вертикальный layout для центрирования по вертикали
        vbox = QVBoxLayout()
        vbox.addStretch(1)  # Прокладка сверху

        # Горизонтальный layout для центрирования по горизонтали
        hbox = QHBoxLayout()
        hbox.addStretch(1)  # Прокладка слева

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)  # Расстояние между кнопками
        self.gridLayout.setContentsMargins(10, 10, 10, 10)  # Отступы от краев

        self.keys = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '←'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
            ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Space']
        ]

        self.key_sizes = {
            '←': (80, 40),
            'Tab': (80, 40),
            'Caps': (80, 40),
            'Enter': (80, 40),
            'Shift': (120, 40),
            'Space': (300, 40),  # Увеличим ширину пробела
            '`': (40, 40),
        }

        self.buttons = []  # Список для хранения кнопок
        self.buttonsDict = {}

        for row, key_row in enumerate(self.keys):
            col_offset = 0
            row_buttons = []
            for col, key in enumerate(key_row):
                button = QPushButton(key)
                width, height = self.key_sizes.get(key, (40, 40))
                button.setFixedSize(width, height)
                button.setStyleSheet(self.get_button_style(key, col))
                if key != 'Space':
                    row_buttons.append(button)
                if key in ['←', 'Enter', 'Shift']:
                    if key == 'Shift' and row == 3:
                        self.gridLayout.addWidget(button, row, col + col_offset, 1, 2)
                        col_offset += 1
                    else:
                        self.gridLayout.addWidget(button, row, col + col_offset, 1, 2)
                        col_offset += 1
                elif key == 'Space':
                    pass
                else:
                    self.gridLayout.addWidget(button, row, col + col_offset)
                self.buttonsDict[key] = [button, col]
            self.buttons.append(row_buttons)

        space_button = QPushButton('Space')
        space_button.setFixedSize(300, 40)  # Увеличенная ширина пробела
        space_button.setStyleSheet(self.get_button_style('Space', 0))
        self.gridLayout.addWidget(space_button, 4, 3, 1, 7)  # Центрирование пробела
        self.buttons[4].append(space_button)

        hbox.addLayout(self.gridLayout)
        hbox.addStretch(1)  # Прокладка справа

        vbox.addLayout(hbox)
        vbox.addStretch(1)  # Прокладка снизу

        self.setLayout(vbox)  # Устанавливаем главный layout

    def get_button_style(self, key, col):
        base_style = """
            QPushButton {
                border-radius: 4px;
                font-size: 16px;
                font-weight: 600;
                padding: 5px;
                border: 2px solid #dddddd;
            }
            QPushButton:hover {
                background-color: #e6e6e6;
            }
            QPushButton:pressed {
                background-color: #d6d6d6;
            }
        """
        if key in ['←', 'Tab', 'Caps', 'Enter', 'Shift', 'Space']:
            special_style = """
                QPushButton {
                    background-color: rgb(219, 226, 229);
                    font-weight: bold;
                }
            """
            return base_style + special_style
        if col % 2 == 0:
            even_style = """
                QPushButton {
                    background-color: rgb(201, 200, 255);
                    color: rgb(44, 43, 107);
                }
            """
            return base_style + even_style
        else:
            odd_style = """
                QPushButton {
                    background-color: rgb(172, 243, 199);
                    color: rgb(23, 113, 58);
                }
            """
            return base_style + odd_style

    def highlightButton(self, key):
        if (len(key)):
            key = key[-1]  # Убираем пробелы с начала и конца строки
        else:
            key = ' '

        # Обработка пробела и преобразование специальных символов
        special_keys = {
            ' ': 'Space',
            '\t': 'Tab',
            '\n': 'Enter',
            '\r': 'Enter',
            '\b': '←',
        }

        if (key in special_keys):
            key = special_keys.get(key)
        else:
            key = key.upper()
        if key in self.buttonsDict:
            buttonCol = self.buttonsDict[key]
            button = buttonCol[0]
            col = buttonCol[1]
            curStyle = self.get_button_style(key, col)
            print(curStyle)
            button.setStyleSheet(curStyle + "QPushButton {background-color: #70a322}")
            QTimer.singleShot(100, lambda: button.setStyleSheet(curStyle))
        else:
            print(f"Клавиша '{key}' не найдена в словаре buttonsDict.")
