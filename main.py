import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer, QTime
from Keyboard import Keyboard
from Input import Input
from Textfield import Textfield


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typing Trainer")

        keyboard = Keyboard()
        textField = Textfield()
        score_label = QLabel()
        self.reload = QPushButton("Restart")
        self.reload.clicked.connect(self.reset)
        self.input = Input(textField, score_label)
        self.input.textEdited.connect(keyboard.highlightButton)

        self.timer = QTimer()  # Основной таймер
        self.timer.setInterval(60000)  # Устанавливаем интервал в 1 минуту

        self.child_timer = QTimer()  # Дочерний таймер
        self.child_timer.setInterval(1000)  # Устанавливаем интервал в 1 секунду

        self.input_started = False
        self.timer_label = QLabel()
        self.current_time = QTime(0, 1)
        self.timer_label.setText(self.current_time.toString("mm:ss"))

        self.input.textChanged.connect(self.startTimer)
        self.timer.timeout.connect(self.endTimer)
        self.child_timer.timeout.connect(self.updateChildTimer)

        self.speed_label = QLabel()
        self.speed_label.setText("0 CPM")
        self.input.textChanged.connect(self.updateSpeedLabel)

        main_layout = QGridLayout()
        main_layout.addWidget(self.speed_label, 0, 0)
        main_layout.addWidget(score_label, 0, 1)
        main_layout.addWidget(self.reload, 0, 2)
        main_layout.addWidget(self.timer_label, 0, 3)
        main_layout.addWidget(textField, 1, 0, 1, 4)
        main_layout.addWidget(self.input, 2, 0, 1, 4)
        main_layout.addWidget(keyboard, 3, 0, alignment=Qt.AlignCenter)
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def updateSpeedLabel(self):
        if self.input_started:
            cur_t = 60 - self.current_time.second()
            print(str(cur_t) + " " + str(self.input.getCorrectLetters()))
            if cur_t != 0:
                cur_speed = self.input.getCorrectLetters() * 60 / cur_t
            else:
                cur_speed = 0
            self.speed_label.setText(str(cur_speed) + " CPM")

    def reset(self):
        self.input.reset()
        self.timer.stop()
        self.child_timer.stop()
        self.current_time = QTime(0, 1)
        self.input_started = False
        self.timer_label.setText(self.current_time.toString("mm:ss"))

    def startTimer(self):
        # Если ввод еще не начался, запускаем таймер
        if not self.input_started:
            self.input_started = True
            self.timer.start()
            self.child_timer.start()  # Запускаем дочерний таймер

    def endTimer(self):
        self.timer.stop()
        self.child_timer.stop()  # Останавливаем дочерний таймер
        self.input_started = False
        self.updateChildTimer()
        print(self.speed_label.text())

    def updateChildTimer(self):
        # Обновляем текущее время и выводим его на QLabel
        self.current_time = self.current_time.addSecs(-1)
        self.timer_label.setText(self.current_time.toString("mm:ss"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
