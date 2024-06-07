import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QSizePolicy, QLineEdit
from PyQt5.QtCore import QSize, Qt, QEvent, ws
from Textfield import Textfield


class Input(QLineEdit):

    def __init__(self, textField, score_label):
        super().__init__()
        self.textfield = textField
        self.score_label = score_label
        self.textChanged.connect(self.checkInput)
        self.current_word_start = 0
        self.correct_words = 0
        self.correct_letters = 0

    def checkInput(self):
        input_text = self.text()
        if input_text and input_text[-1].isspace():
            word = input_text.strip()
            if word:
                cur_word = self.textfield.original_text.split(" ")[0]  # Get the first word
                if word == cur_word:
                    self.correct_words += 1
                    self.correct_letters += len(cur_word)
                    self.score_label.setText(f"Correct Words: {self.correct_words}")
                # Remove the first word and update text
                remaining_text = ' '.join(self.textfield.original_text.split(' ')[1:])
                self.textfield.original_text = remaining_text
                self.textfield.updateText(0)
            self.setText("")

    def getCorrectWords(self):
        return self.correct_words

    def getCorrectLetters(self):
        return self.correct_letters

    def reset(self):
        self.correct_words = 0
        self.correct_letters = 0
        self.current_word_start = 0
        self.score_label.setText(f"Correct Words: {self.correct_words}")
        self.textfield.genText()
