from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis


class WpmChartWindow(QMainWindow):
    def __init__(self, wpm_data):
        super().__init__()

        self.setWindowTitle('График WPM')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        chart_view = QChartView(self)

        self.chart = QChart()
        self.chart.setTitle("График WPM")

        series = QLineSeries()

        # Добавляем данные WPM в график
        for i, wpm in enumerate(wpm_data):
            series.append(i + 1, wpm)

        self.chart.addSeries(series)

        # Настройка осей
        axis_x = QValueAxis()
        axis_x.setLabelFormat('%i')  # Формат меток на оси Ox (целые числа)
        axis_x.setTitleText('Номер записи')
        self.chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText('WPM')
        self.chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        chart_view.setChart(self.chart)
        layout.addWidget(chart_view)

    def update_chart(self, wpm_data):
        self.chart.series()[0].clear()  # Очистка текущих данных
        series = self.chart.series()[0]

        # Добавление новых данных WPM в график
        for i, wpm in enumerate(wpm_data):
            series.append(i + 1, wpm)