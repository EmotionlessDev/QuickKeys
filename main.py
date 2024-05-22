import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout
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
        # self.setFixedSize(600, 400)

        # self.display_text = DisplayText(self)
        # self.typing_filter = TypingFilter(self.display_text, self)
        # self.typing_filter.set_level_text(english_levels_1[0])

        keyboard = Keyboard()
        input = Input() 
        textField = Textfield()
        input.input.textEdited.connect(keyboard.highlightButton)
        main_layout = QGridLayout()
        # main_layout.addWidget(self.display_text, 0, 0)
        # main_layout.addWidget(self.typing_filter, 1, 0)
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
