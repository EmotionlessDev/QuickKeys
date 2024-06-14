import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QDialog, QTabWidget
from PyQt5.QtCore import Qt
from Keyboard import Keyboard
from StatisticTab import StatisticsTab
from Textfield import Textfield
from TypingSession import TypingSession
from MainLayout import MainLayout
from UserDialog import UserDialog
import qdarkgraystyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typing Trainer")

        user_dialog = UserDialog(self)
        self.user_id = None
        if user_dialog.exec_() == QDialog.Accepted:
            self.user_id = user_dialog.current_user_id
            self.init_ui()
        else:
            sys.exit()  # Закрываем приложение, если пользователь не вошел

    def init_ui(self):
        # Инициализация виджетов
        keyboard = Keyboard()
        textField = Textfield()
        self.score_label = QLabel()
        self.timer_label = QLabel()
        self.speed_label = QLabel("0 CPM")
        self.reload_button = QPushButton("Restart")

        # Кнопка регистрации пользователя
        self.register_button = QPushButton("Register User")
        self.register_button.clicked.connect(self.show_registration_dialog)

        # Создаем и инициализируем TypingSession
        self.typing_session = TypingSession(
            self.user_id,
            textfield=textField,
            timer_label=self.timer_label,
            speed_label=self.speed_label,
            reset_button=self.reload_button,
            callback_end=self.endSession
        )

        # Подключаем сигнал highlightButton к методу keyboard.highlightButton
        self.typing_session.input.textEdited.connect(keyboard.highlightButton)

        # Создание вкладок
        self.tabs = QTabWidget()

        # Создание виджетов для каждой вкладки
        self.typing_session = MainLayout(
            speed_label=self.speed_label,
            score_label=self.score_label,
            reload_button=self.reload_button,
            timer_label=self.timer_label,
            textField=textField,
            input=self.typing_session.input,
            keyboard=keyboard
        ).create_layout()
        self.statistics_tab = StatisticsTab(self.user_id)

        # Добавление виджетов в QTabWidget
        self.tabs.addTab(self.typing_session, "Тренировка")
        self.tabs.addTab(self.statistics_tab, "Статистика")

        # Установка QTabWidget в качестве центрального виджета
        self.setCentralWidget(self.tabs)

    def show_registration_dialog(self):
        dialog = UserDialog(self)
        dialog.exec_()  # Открываем диалоговое окно регистрации

    def endSession(self):
        """Вызывается при завершении таймерной сессии"""
        self.statistics_tab.load_statistics()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
