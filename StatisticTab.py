from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from StatisticsManager import StatisticsManager
from WpmChartWindow import WpmChartWindow


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

    # to do: Обновлять данные в графике, вместо того, чтобы создавать его заново
    def load_statistics(self):
        user_id = self.user_id
        stats = self.statistics_manager.fetch_statistics(user_id)

        wpm_data = []
        self.stats_list.clear()
        id = 1
        for record in stats:
            cpm, wpm, errors, timestamp = record
            wpm_data.append(int(wpm))
            stat_entry = f"ID: {id} \t CPM: {int(cpm)} \t WPM: {int(wpm)} \t Errors: {errors} \t Time: {timestamp}"
            self.stats_list.addItem(stat_entry)
            id += 1
        self.layout.removeWidget(self.chart)
        self.chart = WpmChartWindow(wpm_data)
        self.layout.addWidget(self.chart)
