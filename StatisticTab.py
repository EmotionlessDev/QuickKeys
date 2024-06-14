from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from StatisticsManager import StatisticsManager


class StatisticsTab(QWidget):
    def __init__(self, current_user_id: int):
        super().__init__()
        self.initUI()
        self.user_id = current_user_id
        self.statistics_manager = StatisticsManager()
        self.load_statistics()

    def initUI(self):
        layout = QVBoxLayout()

        self.stats_label = QLabel("История статистики:", self)
        self.stats_list = QListWidget(self)

        layout.addWidget(self.stats_label)
        layout.addWidget(self.stats_list)

        self.setLayout(layout)

    def load_statistics(self):
        user_id = self.user_id
        stats = self.statistics_manager.fetch_statistics(user_id)

        for record in stats:
            cpm, wpm, errors, timestamp = record
            stat_entry = f"CPM: {cpm}, WPM: {wpm}, Errors: {errors}, Time: {timestamp}"
            self.stats_list.addItem(stat_entry)
