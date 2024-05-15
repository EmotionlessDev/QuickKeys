import sys, os, csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QGridLayout, QHBoxLayout, QLabel, QCheckBox, QRadioButton, QButtonGroup, QTableWidget, QTableWidgetItem, QFileDialog, QComboBox
from PyQt5.QtGui import QFont
from Keyboard import Keyboard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickKeys")
        keyboard = Keyboard()
        main_layout = QVBoxLayout()
        main_layout.addWidget(keyboard)
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
