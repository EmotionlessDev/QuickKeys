from PyQt5.Qt import QKeySequence
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QKeyEvent, QColor, QPalette

DISPLAY_TEXT_LENGTH = 10

class TypingFilter(QLineEdit):
    game_ended = pyqtSignal()
    right_input = pyqtSignal(int)

    def __init__(self, display_text_widget, parent=None):
        super().__init__(parent)
        self.display_text_widget = display_text_widget
        self.level_text = ''
        self.is_game_end = False
        self.textChanged.connect(self.input_filter)

    def switch_input(self, switch: bool):
        self.setEnabled(switch)

    def set_level_text(self, text):
        self.setText('')
        self.level_text = text
        self.display_text_widget.set_level_text(text)

    def get_level_text(self):
        return self.level_text

    def input_filter(self):
        text = self.text()
        if not text:
            return

        last_symb = text[-1]
        if self.level_text[len(text) - 1] != last_symb:
            self.setText(text[:-1])
            self.set_wrong_input_color()
            return

        self.set_correct_input_color()

        if last_symb == ' ' or len(text) >= DISPLAY_TEXT_LENGTH:
            if text.strip() == self.level_text[:len(text)].strip():
                self.right_input.emit(len(text))
                self.level_text = self.level_text[len(text):].lstrip()
                self.setText('')
                self.display_text_widget.update_text_displayment(len(text))
                if not self.level_text:
                    self.game_ended.emit()
                return

    def keyPressEvent(self, event: QKeyEvent):
        if event.matches(QKeySequence.Paste):
            event.ignore()
        else:
            super().keyPressEvent(event)

    def set_wrong_input_color(self):
        palette = self.palette()
        palette.setColor(QPalette.Text, QColor('red'))
        self.setPalette(palette)

    def set_correct_input_color(self):
        palette = self.palette()
        palette.setColor(QPalette.Text, QColor('gray'))
        self.setPalette(palette)
