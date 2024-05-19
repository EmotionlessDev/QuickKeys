import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from window import TypingFilter
from Text import DisplayText
from Keyboard import Keyboard
from Englelvls import english_levels_2, english_levels_1

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typing Trainer")
        self.setFixedSize(600, 400)

        self.display_text = DisplayText(self)
        self.typing_filter = TypingFilter(self.display_text, self)
        self.typing_filter.set_level_text(english_levels_1[0])


        keyboard = Keyboard()

        layout = QVBoxLayout()
        layout.addWidget(self.display_text)
        layout.addWidget(self.typing_filter)
        layout.addWidget(keyboard)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
