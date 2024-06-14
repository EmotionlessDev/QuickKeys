from PyQt5.QtCore import QTime, pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton
from TypingTimer import TypingTimer
from Input import Input
from Textfield import Textfield
from StatisticsManager import StatisticsManager


class TypingSession:
    def __init__(self, user_id, textfield: Textfield, timer_label: QLabel, speed_label: QLabel, reset_button: QPushButton,
                 callback_end):
        self.user_id = user_id
        self.textfield = textfield
        self.timer_label = timer_label
        self.speed_label = speed_label
        self.speed = 0
        self.reset_button = reset_button
        self.callback_end = callback_end
        self.statistic = StatisticsManager()

        self.score_label = QLabel()  # Метка для отображения счета
        self.input = Input(textfield, self.score_label)

        # Инициализация таймера для сессии
        self.typing_timer = TypingTimer(self.timer_label, self.endSession, 30000)

        self.input_started = False
        self.input.textChanged.connect(self.startTimer)
        self.typing_timer.child_timer.timeout.connect(self.updateSpeedLabel)
        self.reset_button.clicked.connect(self.resetSession)

    def updateSpeedLabel(self):
        if self.input_started:
            # Определяем прошедшее время с момента начала ввода
            elapsed_time = (self.typing_timer.initial_milliseconds - self.typing_timer.remaining_time) / 1000  # в секундах
            if elapsed_time > 0:
                # Получаем количество правильно введенных символов
                correct_letters = self.input.getCorrectLetters()
                # Рассчитываем скорость ввода в символах в минуту (CPM)
                cur_speed = (correct_letters * 60) / elapsed_time
                self.speed = cur_speed
                # Обновляем метку скорости
                self.speed_label.setText(f"{cur_speed:.2f} CPM")
            else:
                self.speed_label.setText("0.00 CPM")  # Если время еще не прошло, показываем 0 CPM

    def resetSession(self):
        self.input.reset()
        self.input.unblock()
        self.typing_timer.reset()  # Сброс таймера
        self.input_started = False

    def startTimer(self):
        if not self.input_started:
            self.input_started = True
            self.typing_timer.start()

    def endSession(self):
        self.statistic.record_statistics(self.user_id, int(self.speed), int(self.speed/4), self.input.errors)
        self.callback_end()  # Вызываем callback по окончании сессии
        self.input.reset()
        self.input.block()
        self.input_started = False
        self.typing_timer.stop()
        self.updateSpeedLabel()  # Обновляем метку скорости в конце сессии
