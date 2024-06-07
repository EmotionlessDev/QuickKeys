from PyQt5.QtCore import QTime, pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton
from TypingTimer import TypingTimer
from Input import Input  # Предполагаем, что этот класс уже реализован
from Textfield import Textfield  # Предполагаем, что этот класс уже реализован


class TypingSession:
    def __init__(self, textfield: Textfield, timer_label: QLabel, speed_label: QLabel, reset_button: QPushButton,
                 callback_end):
        self.textfield = textfield
        self.timer_label = timer_label
        self.speed_label = speed_label
        self.reset_button = reset_button
        self.callback_end = callback_end

        self.score_label = QLabel()  # Метка для отображения счета
        self.input = Input(textfield, self.score_label)

        # Инициализация таймера для сессии
        self.typing_timer = TypingTimer(self.timer_label, self.endSession)

        self.input_started = False
        self.input.textChanged.connect(self.startTimer)
        self.input.textChanged.connect(self.updateSpeedLabel)
        self.reset_button.clicked.connect(self.resetSession)

    def updateSpeedLabel(self):
        if self.input_started:
            cur_t = 60 - self.typing_timer.current_time.second()
            if cur_t != 0:
                cur_speed = self.input.getCorrectLetters() * 60 / cur_t
            else:
                cur_speed = 0
            self.speed_label.setText(f"{cur_speed:.2f} CPM")

    def resetSession(self):
        self.input.reset()
        self.typing_timer.reset()  # Сброс таймера
        self.input_started = False

    def startTimer(self):
        if not self.input_started:
            self.input_started = True
            self.typing_timer.start()

    def endSession(self):
        self.input_started = False
        self.typing_timer.stop()
        self.updateSpeedLabel()  # Обновляем метку скорости в конце сессии
        self.callback_end()  # Вызываем callback по окончании сессии
