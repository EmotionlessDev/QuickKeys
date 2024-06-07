import sys
import random
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
        self.words = "the be to of and a in that have I it for not on with he as you do at this but his by from they we say her she or an will my one all would there their what so up out if about who get which go me when make can like time no just him know take people into year your good some could them see other than now look only come its over think also back after use two how our work first well way even new want because any these give day most us are was were has been had did should may might must shall get find long part those between still call off air animal at back before being below best both came come different does down even first found help here how if into is it just know large last learn leave left line little look made make many more much must never number often only or own place put read right same saw show since small something sound such take tell than that their them then thing think though thought three through together too under until water were where while who would year your"
        self.setText(self.words) 
        self.setCursorPosition(0)
        self.original_text = self.text()

    def updateText(self, start):
        self.setText(self.original_text[start:])
        self.setCursorPosition(0)
    
    def genText(self):
        words = self.words.split()
        selected_words = ""
        for i in range(400):
            index = random.randint(0, len(words) - 1)
            selected_words += words[index] + ' '  # Добавляем слово к selected_words
        self.setText(selected_words.strip())  # Устанавливаем сгенерированный текст
        self.original_text = self.text()
        self.setCursorPosition(0)  # Устанавливаем позицию курсора в начало
