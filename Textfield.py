import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QSizePolicy, QLineEdit
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QRect
from PyQt5.QtCore import QSize

class Textfield(QWidget):
    def __init__(self): 
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        layout.addLayout(self.gridLayout)
        self.setLayout(layout)
        self.textField = QLineEdit()
        self.textField.setReadOnly(True)
        self.gridLayout.addWidget(self.textField, 0, 0)


    

