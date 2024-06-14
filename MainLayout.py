from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class MainLayout:
    def __init__(self, speed_label: QLabel, score_label: QLabel, reload_button: QPushButton, mode_button: QPushButton,
                 timer_label: QLabel,
                 textField, input, keyboard):
        self.speed_label = speed_label
        self.score_label = score_label
        self.reload_button = reload_button
        self.mode_button = mode_button
        self.timer_label = timer_label
        self.textField = textField
        self.input = input
        self.keyboard = keyboard

    def create_layout(self) -> QWidget:
        """
        Создает и возвращает виджет с основным макетом.
        :return: QWidget с установленным макетом.
        """
        # Верхняя панель с лейблами и кнопками
        top_layout = QHBoxLayout()

        # Лейблы выравнены влево
        labels_layout = QHBoxLayout()
        labels_layout.addWidget(self.speed_label)
        labels_layout.addWidget(self.score_label)
        labels_layout.addStretch(1)  # Добавляем растяжку, чтобы кнопки и таймер ушли вправо

        # Кнопки и таймер выравнены вправо
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.mode_button)
        buttons_layout.addWidget(self.reload_button)
        buttons_layout.addWidget(self.timer_label)

        # Добавляем обе части в top_layout
        top_layout.addLayout(labels_layout)
        top_layout.addLayout(buttons_layout)

        # Центральная часть с текстовыми полями
        middle_layout = QVBoxLayout()
        middle_layout.addWidget(self.textField)
        middle_layout.addWidget(self.input)

        # Нижняя панель с клавиатурой
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch(1)  # Добавляем отступы для центрирования клавиатуры
        bottom_layout.addWidget(self.keyboard, alignment=Qt.AlignCenter)
        bottom_layout.addStretch(1)  # Добавляем отступы для центрирования клавиатуры

        # Основной вертикальный макет
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(bottom_layout)

        container = QWidget()
        container.setLayout(main_layout)

        # Настройка отступов и интервалов
        main_layout.setContentsMargins(10, 10, 10, 10)  # Устанавливаем отступы от краев окна
        main_layout.setSpacing(10)  # Устанавливаем интервалы между элементами

        return container
