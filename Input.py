import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QSizePolicy, QLineEdit
from PyQt5.QtCore import QSize, Qt


class Input(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFocusPolicy(Qt.StrongFocus)  # Установка политики фокусировки

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.input = QLineEdit()
        layout.addWidget(self.input)
        

