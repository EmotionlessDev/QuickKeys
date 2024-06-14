from PyQt5.QtCore import QTimer, QTime, QTimeZone, QDateTime
from PyQt5.QtWidgets import QLabel

class TypingTimer:
    def __init__(self, timer_label: QLabel, callback_end, initial_milliseconds: int = 60000):
        """
        :param timer_label: QLabel для отображения времени таймера.
        :param callback_end: Функция обратного вызова, которая вызывается при завершении таймера.
        :param initial_milliseconds: Количество миллисекунд для начального времени таймера.
        """
        self.timer_label = timer_label
        self.callback_end = callback_end
        self.initial_milliseconds = initial_milliseconds

        self.main_timer = QTimer()
        self.main_timer.setInterval(initial_milliseconds)
        self.main_timer.timeout.connect(self.endTimer)

        self.child_timer = QTimer()
        self.child_timer.setInterval(1000)  # Интервал дочернего таймера в 1 секунду
        self.child_timer.timeout.connect(self.updateChildTimer)

        self.remaining_time = initial_milliseconds  # Начальное время в миллисекундах
        self.timer_label.setText(self.format_time(self.remaining_time))
        self.timer_running = False

    def start(self):
        """Запускает основной и дочерний таймеры."""
        if not self.timer_running:
            self.timer_running = True
            self.main_timer.start(self.remaining_time)  # Начинаем основной таймер с текущего оставшегося времени
            self.child_timer.start()

    def stop(self):
        """Останавливает основной и дочерний таймеры."""
        self.main_timer.stop()
        self.child_timer.stop()
        self.timer_running = False

    def reset(self, milliseconds: int = None):
        """Сбрасывает таймер и обновляет метку времени."""
        self.stop()
        if milliseconds is not None:
            self.initial_milliseconds = milliseconds
        self.remaining_time = self.initial_milliseconds  # Сбрасываем на заданное количество миллисекунд
        self.timer_label.setText(self.format_time(self.remaining_time))

    def updateChildTimer(self):
        """Обновляет метку времени каждую секунду."""
        self.remaining_time -= 1000  # Уменьшаем оставшееся время на 1 секунду (1000 миллисекунд)
        self.timer_label.setText(self.format_time(self.remaining_time))
        if self.remaining_time <= 0:
            self.endTimer()

    def endTimer(self):
        """Вызывается по окончании основного таймера."""
        self.stop()
        self.remaining_time = 0
        self.timer_label.setText("00:00")  # Обновляем метку времени до нуля
        self.callback_end()  # Вызываем обратный вызов

    def format_time(self, milliseconds: int) -> str:
        """Форматирует время в миллисекундах в строку 'mm:ss'."""
        seconds = milliseconds // 1000
        minutes = seconds // 60
        seconds %= 60
        return f"{minutes:02}:{seconds:02}"
