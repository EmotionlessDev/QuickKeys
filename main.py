import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt
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
        input = Input(textField, score_label) 
        input.textEdited.connect(keyboard.highlightButton)
        main_layout = QGridLayout()
        main_layout.addWidget(score_label, 0, 0)
        main_layout.addWidget(textField, 1, 0)
        main_layout.addWidget(input, 2, 0)
        main_layout.addWidget(keyboard, 3, 0, alignment=Qt.AlignCenter)
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
