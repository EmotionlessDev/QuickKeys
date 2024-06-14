from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QLabel

class TypingTimer:
    def __init__(self, timer_label: QLabel, callback_end, initial_minutes: int = 1):
        """
        :param timer_label: QLabel для отображения времени таймера.
        :param callback_end: Функция обратного вызова, которая вызывается при завершении таймера.
        :param initial_minutes: Количество минут для начального времени таймера.
        """
        self.timer_label = timer_label
        self.callback_end = callback_end
        self.initial_minutes = initial_minutes

        self.main_timer = QTimer()
        self.main_timer.setInterval(initial_minutes * 60000)  # Интервал основного таймера в заданные минуты
        self.main_timer.timeout.connect(self.endTimer)

        self.child_timer = QTimer()
        self.child_timer.setInterval(1000)  # Интервал дочернего таймера в 1 секунду
        self.child_timer.timeout.connect(self.updateChildTimer)

        self.current_time = QTime(0, initial_minutes)  # Начальное время
        self.timer_label.setText(self.current_time.toString("mm:ss"))
        self.timer_running = False

    def start(self):
        """Запускает основной и дочерний таймеры."""
        if not self.timer_running:
            self.timer_running = True
            self.main_timer.start(self.current_time.msecsSinceStartOfDay())  # Начинаем основной таймер с текущего времени
            self.child_timer.start()

    def stop(self):
        """Останавливает основной и дочерний таймеры."""
        self.main_timer.stop()
        self.child_timer.stop()
        self.timer_running = False

    def reset(self, minutes: int = None):
        """Сбрасывает таймер и обновляет метку времени."""
        self.stop()
        if minutes is not None:
            self.initial_minutes = minutes
        self.current_time = QTime(0, self.initial_minutes)  # Сбрасываем на заданное количество минут
        self.timer_label.setText(self.current_time.toString("mm:ss"))

    def updateChildTimer(self):
        """Обновляет метку времени каждую секунду."""
        self.current_time = self.current_time.addSecs(-1)
        self.timer_label.setText(self.current_time.toString("mm:ss"))
        if self.current_time == QTime(0, 0, 0):
            self.endTimer()

    def endTimer(self):
        """Вызывается по окончании основного таймера."""
        self.stop()
        self.timer_label.setText("00:00")  # Обновляем метку времени до нуля
        self.callback_end()  # Вызываем обратный вызов
