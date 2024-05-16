import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PyQt5.QtCore import Qt
from Keyboard import Keyboard
from Input import Input


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickKeys")
        keyboard = Keyboard()
        input = Input() 
        main_layout = QGridLayout()
        main_layout.addWidget(input, 0, 0)
        main_layout.addWidget(keyboard, 1, 0, alignment=Qt.AlignCenter)
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 
