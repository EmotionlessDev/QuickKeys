from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout, QTabWidget, \
    QWidget
from DataBase import Database


class UserDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("User Authentication")

        # Создание вкладок для регистрации и входа
        self.tabs = QTabWidget()
        self.login_tab = QWidget()
        self.register_tab = QWidget()

        self.create_login_tab()
        self.create_register_tab()

        self.tabs.addTab(self.login_tab, "Login")
        self.tabs.addTab(self.register_tab, "Register")

        # Основная компоновка
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def create_login_tab(self):
        """Создает вкладку для входа"""
        login_layout = QFormLayout()

        self.login_username_input = QLineEdit()
        self.login_password_input = QLineEdit()
        self.login_password_input.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login_user)

        login_layout.addRow("Username:", self.login_username_input)
        login_layout.addRow("Password:", self.login_password_input)
        login_layout.addWidget(login_button)

        self.login_tab.setLayout(login_layout)

    def create_register_tab(self):
        """Создает вкладку для регистрации"""
        register_layout = QFormLayout()

        self.register_username_input = QLineEdit()
        self.register_password_input = QLineEdit()
        self.register_password_input.setEchoMode(QLineEdit.Password)

        register_button = QPushButton("Register")
        register_button.clicked.connect(self.register_user)

        register_layout.addRow("Username:", self.register_username_input)
        register_layout.addRow("Password:", self.register_password_input)
        register_layout.addWidget(register_button)

        self.register_tab.setLayout(register_layout)

    def login_user(self):
        """Обрабатывает вход пользователя"""
        username = self.login_username_input.text()
        password = self.login_password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Both fields are required!")
            return

        db = Database("users.db")  # Используем отдельную базу данных для пользователей
        try:
            db.cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = db.cursor.fetchone()
            if result and result[0] == password:
                QMessageBox.information(self, "Success", "Login successful!")
                self.accept()
            else:
                QMessageBox.warning(self, "Login Failed", "Incorrect username or password.")
        except Exception as e:
            QMessageBox.critical(self, "Login Error", str(e))
        finally:
            db.close()

    def register_user(self):
        """Обрабатывает регистрацию нового пользователя"""
        username = self.register_username_input.text()
        password = self.register_password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Both fields are required!")
            return

        db = Database("users.db")  # Используем отдельную базу данных для пользователей
        try:
            db.create_table("users", "username TEXT PRIMARY KEY, password TEXT")
            db.insert_data("users", (username, password))
            QMessageBox.information(self, "Success", "User registered successfully!")
            self.accept()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Registration Failed", "Username already exists.")
        except Exception as e:
            QMessageBox.critical(self, "Registration Error", str(e))
        finally:
            db.close()

    def closeEvent(self, event):
        """Закрытие окна без сохранения данных"""
        reply = QMessageBox.question(self, 'Confirm Exit',
                                     'Are you sure you want to exit without saving?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
