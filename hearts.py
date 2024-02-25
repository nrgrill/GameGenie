import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt

class MyTable(QTableWidget):
    def __init__(self, data, result_labels, rounds):
        super().__init__()
        self.rounds = rounds
        self.passing = ["Center", "Left", "Right"]
        self.passing_order = [QLabel(self.passing[self.rounds % len(self.passing)])]

        self.setRowCount(len(data))
        self.setColumnCount(len(data[0]))
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                item_widget = QTableWidgetItem(str(item))
                item_widget.setFlags(item_widget.flags() | Qt.ItemFlag.ItemIsEditable)
                self.setItem(i, j, item_widget)

        self.itemChanged.connect(self.update_totals)

    def update_round_label(self):
        self.passing_order[0].setText(self.passing[self.rounds % len(self.passing)])

    def update_totals(self, item):
        total = 0
        column_index = item.column()
        for i in range(self.rowCount()):
            try:
                total += int(self.item(i, column_index).text())
            except ValueError:
                pass
        self.result_labels[column_index].setText(f"Player {column_index + 1} Score: {total}")

    def add_row_button_clicked(self):
        current_row_count = self.rowCount()
        self.insertRow(current_row_count)
        for j in range(self.columnCount()):
            item_widget = QTableWidgetItem("0")
            item_widget.setFlags(item_widget.flags() | Qt.ItemFlag.ItemIsEditable)
            self.setItem(current_row_count, j, item_widget)

        for column_index in range(self.columnCount()):
            self.update_totals(self.item(current_row_count, column_index))

        self.rounds += 1
        self.update_round_label()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.tab_widget = QTabWidget(self.central_widget)

        self.home = QWidget()
        self.setup_home()
        self.euchre = QWidget()
        self.setup_euchre()
        self.Hearts = QWidget()
        self.setup_hearts()
        self.list_of_games = QWidget()
        self.setup_list_of_games()

        self.tab_widget.addTab(self.home, "Home")
        self.tab_widget.addTab(self.euchre, "Euchre")
        self.tab_widget.addTab(self.Hearts, "Hearts")
        self.tab_widget.addTab(self.list_of_games, "List Of Games")

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.tab_widget)

        default_width = 800
        default_height = 600
        self.resize(default_width, default_height)

    def setup_home(self):
        label = QLabel("GameGenie")
        layout = QVBoxLayout(self.home)
        layout.addWidget(label)
        button = QPushButton("Start Playing")
        button.clicked.connect(lambda: self.tab_widget.setCurrentIndex(3))
        layout.addWidget(button)

    def setup_euchre(self):
        label = QLabel("Content of Page 1")
        layout = QVBoxLayout(self.euchre)
        layout.addWidget(label)

    def setup_hearts(self):
        data = [[0, 0, 0, 0]]
        result_labels = [QLabel(f"Player {i + 1} Score: 0") for i in range(4)]
        table = MyTable(data, result_labels, rounds=0)

        layout = QVBoxLayout(self.Hearts)
        layout.addWidget(table)

        for label in result_labels:
            layout.addWidget(label)

        round_label = QLabel(f"Passing: {table.passing_order[0].text()}")
        layout.addWidget(round_label)

        add_row_button = QPushButton("Add Row")
        add_row_button.clicked.connect(table.add_row_button_clicked)
        layout.addWidget(add_row_button)

    def setup_list_of_games(self):
        label = QLabel("Content of Page 3")
        button = QPushButton("Euchre")
        button.clicked.connect(lambda: self.tab_widget.setCurrentIndex(1))
        button1 = QPushButton("Hearts")
        button1.clicked.connect(lambda: self.tab_widget.setCurrentIndex(2))
        layout = QVBoxLayout(self.list_of_games)
        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(button1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
