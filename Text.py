from PyQt5.QtWidgets import QLineEdit

DISPLAY_TEXT_LENGTH = 10

class DisplayText(QLineEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.start = 0
        self.full_text = ''

    def set_level_text(self, text: str):
        self.start = 0
        self.full_text = text
        self.update_text_displayment(0)

    def get_level_text(self):
        return self.full_text

    def update_text_displayment(self, step: int):
        self.start += step
        if self.start < 0:
            self.start = 0
        if self.start >= len(self.full_text):
            self.start = len(self.full_text) - 1
        self.setText(self.full_text[self.start:self.start + DISPLAY_TEXT_LENGTH])
