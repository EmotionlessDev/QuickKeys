import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt
from Keyboard import Keyboard
from Textfield import Textfield
from TypingSession import TypingSession
from MainLayout import MainLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typing Trainer")

        # Инициализация виджетов
        keyboard = Keyboard()
        textField = Textfield()
        self.score_label = QLabel()
        self.timer_label = QLabel()
        self.speed_label = QLabel("0 CPM")
        self.reload_button = QPushButton("Restart")

        # Создаем и инициализируем TypingSession
        self.typing_session = TypingSession(
            textfield=textField,
            timer_label=self.timer_label,
            speed_label=self.speed_label,
            reset_button=self.reload_button,
            callback_end=self.endSession
        )

        # Подключаем сигнал highlightButton к методу keyboard.highlightButton
        self.typing_session.input.textEdited.connect(keyboard.highlightButton)

        # Создаем и устанавливаем основной макет
        main_layout = MainLayout(
            speed_label=self.speed_label,
            score_label=self.score_label,
            reload_button=self.reload_button,
            timer_label=self.timer_label,
            textField=textField,
            input=self.typing_session.input,
            keyboard=keyboard
        )

        self.setCentralWidget(main_layout.create_layout())

    def endSession(self):
        """Вызывается при завершении таймерной сессии"""
        print(self.speed_label.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
