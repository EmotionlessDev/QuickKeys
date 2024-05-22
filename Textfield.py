import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QSizePolicy, QLineEdit
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QRect
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor, QTextCursor, QTextCharFormat

class Textfield(QLineEdit):
    def __init__(self): 
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setReadOnly(True)
        self.setText("the be to of and a in that have I it for not on with he as you do at this but his by from they we say her she or an will my one all would there their what so up out if about who get which go me when make can like time no just him know take people into year your good some could them see other than then now look only come its over think also back after use two how our work first well way even new want because any these give day most us")
        self.setCursorPosition(0)
        self.correct_format = QTextCharFormat()
        self.correct_format.setForeground(QColor('green'))
        self.incorrect_format = QTextCharFormat()
        self.incorrect_format.setForeground(QColor('red'))
        self.original_text = self.text()
        self.formatted_text = self.original_text

    def updateText(self, start):
        self.setText(self.original_text[start:])
        self.setCursorPosition(0)
