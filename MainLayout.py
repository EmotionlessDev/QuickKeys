from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt


class MainLayout:
    def __init__(self, speed_label: QLabel, score_label: QLabel, reload_button: QPushButton, timer_label: QLabel,
                 textField, input, keyboard):
        self.speed_label = speed_label
        self.score_label = score_label
        self.reload_button = reload_button
        self.timer_label = timer_label
        self.textField = textField
        self.input = input
        self.keyboard = keyboard

    def create_layout(self) -> QWidget:
        """
        Создает и возвращает виджет с основным макетом.
        :return: QWidget с установленным макетом.
        """
        main_layout = QGridLayout()
        main_layout.addWidget(self.speed_label, 0, 0)
        main_layout.addWidget(self.score_label, 0, 1)
        main_layout.addWidget(self.reload_button, 0, 2)
        main_layout.addWidget(self.timer_label, 0, 3)
        main_layout.addWidget(self.textField, 1, 0, 1, 4)
        main_layout.addWidget(self.input, 2, 0, 1, 4)
        main_layout.addWidget(self.keyboard, 3, 0, alignment=Qt.AlignCenter)

        container = QWidget()
        container.setLayout(main_layout)
        return container
