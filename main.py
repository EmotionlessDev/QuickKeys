import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from window import TypingFilter
from Text import DisplayText
from Keyboard import Keyboard
from Englelvls import english_levels_2, english_levels_1
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
        main_layout = QGridLayout()
        main_layout.addWidget(score_label, 0, 0)
        main_layout.addWidget(self.reload, 0, 1)
        main_layout.addWidget(textField, 1, 0, 1, 2)
        main_layout.addWidget(self.input, 2, 0, 1, 2)
        main_layout.addWidget(keyboard, 3, 0, alignment=Qt.AlignCenter)
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def reset(self):
       self.input.reset() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
