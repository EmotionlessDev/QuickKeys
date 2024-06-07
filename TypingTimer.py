from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QLabel

class TypingTimer:
    def __init__(self, timer_label: QLabel, callback_end):
        """
        :param timer_label: QLabel для отображения времени таймера.
        :param callback_end: Функция обратного вызова, которая вызывается при завершении таймера.
        """
        self.timer_label = timer_label
        self.callback_end = callback_end

        self.main_timer = QTimer()
        self.main_timer.setInterval(60000)  # Интервал основного таймера в 1 минуту
        self.main_timer.timeout.connect(self.endTimer)

        self.child_timer = QTimer()
        self.child_timer.setInterval(1000)  # Интервал дочернего таймера в 1 секунду
        self.child_timer.timeout.connect(self.updateChildTimer)

        self.current_time = QTime(0, 1)  # Начальное время 1 минута
        self.timer_label.setText(self.current_time.toString("mm:ss"))
        self.timer_running = False

    def start(self):
        """Запускает основной и дочерний таймеры."""
        if not self.timer_running:
            self.timer_running = True
            self.main_timer.start()
            self.child_timer.start()

    def stop(self):
        """Останавливает основной и дочерний таймеры."""
        self.main_timer.stop()
        self.child_timer.stop()
        self.timer_running = False

    def reset(self):
        """Сбрасывает таймер и обновляет метку времени."""
        self.stop()
        self.current_time = QTime(0, 1)  # Сбрасываем на 1 минуту
        self.timer_label.setText(self.current_time.toString("mm:ss"))

    def updateChildTimer(self):
        """Обновляет метку времени каждую секунду."""
        self.current_time = self.current_time.addSecs(-1)
        self.timer_label.setText(self.current_time.toString("mm:ss"))

    def endTimer(self):
        """Вызывается по окончании основного таймера."""
        self.stop()
        self.updateChildTimer()  # Обновляем метку времени до нуля
        self.callback_end()  # Вызываем обратный вызов
