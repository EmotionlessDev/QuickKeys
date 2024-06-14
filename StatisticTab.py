from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from StatisticsManager import StatisticsManager
from WpmChartWindow import WpmChartWindow
import sip


class StatisticsTab(QWidget):
    def __init__(self, current_user_id: int):
        super().__init__()
        self.initUI()
        self.user_id = current_user_id
        self.statistics_manager = StatisticsManager()
        self.load_statistics()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.stats_label = QLabel("История статистики:", self)
        self.stats_list = QListWidget(self)
        self.chart = WpmChartWindow([15, 20, 50])

        self.layout.addWidget(self.chart)
        self.layout.addWidget(self.stats_label)
        self.layout.addWidget(self.stats_list)

        self.setLayout(self.layout)

    def load_statistics(self):
        user_id = self.user_id
        stats = self.statistics_manager.fetch_statistics(user_id)

        wpm_data = []
        for record in stats:
            cpm, wpm, errors, timestamp = record
            wpm_data.append(int(wpm))
            stat_entry = f"CPM: {cpm}, WPM: {wpm}, Errors: {errors}, Time: {timestamp}"
            self.stats_list.addItem(stat_entry)
        self.layout.removeWidget(self.chart)
        self.chart = WpmChartWindow(wpm_data)
        self.layout.addWidget(self.chart)
