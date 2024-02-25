import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, QFile, QTextStream
from PySide6.QtGui import QPixmap
from euchre import create_tournament

passing = ["Center", "Left", "Right"]

class HeartsTable(QTableWidget):
    def __init__(self, data, result_labels, passing_label):
        super().__init__()

        self.result_labels = result_labels
        self.passing_label = passing_label
        self.rounds = 1  # Initialize rounds
        self.setRowCount(len(data))
        self.setColumnCount(len(data[0]))
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                item_widget = QTableWidgetItem(str(item))
                item_widget.setFlags(item_widget.flags() | Qt.ItemFlag.ItemIsEditable)
                self.setItem(i, j, item_widget)
        self.itemChanged.connect(self.update_totals)

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

        # Update the passing logic
        self.rounds += 1
        passing_order = passing[self.rounds % len(passing)]
        self.passing_label.setText(f"Passing Order: {passing_order}")

class EuchreTable(QTableWidget):
    def __init__(self, names_array, print_array, result_label):
        super().__init__()

        self.setColumnCount(1)
        self.names_array = names_array
        self.print_array = print_array
        self.result_label = result_label  # New result_label attribute
        self.setHorizontalHeaderLabels(["Names"])
        self.setRowCount(len(names_array))
        for i, name in enumerate(names_array):
            item_widget = QTableWidgetItem(name)
            item_widget.setFlags(item_widget.flags() | Qt.ItemFlag.ItemIsEditable)
            self.setItem(i, 0, item_widget)

        self.itemChanged.connect(self.update_print_array)

    def add_name_button_clicked(self):
        current_row_count = self.rowCount()
        self.insertRow(current_row_count)
        default_name = "Player"
        item_widget = QTableWidgetItem(default_name)
        item_widget.setFlags(item_widget.flags() | Qt.ItemFlag.ItemIsEditable)
        self.setItem(current_row_count, 0, item_widget)
        self.names_array.append(default_name)
        self.update_print_array()

    def update_print_array(self, item):
        self.names_array = [self.item(i, 0).text() for i in range(self.rowCount())]
        names_string = ", ".join(self.names_array)
        self.print_array[0].setText(f"Names: {names_string}")

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
        self.hearts = QWidget()
        self.setup_hearts()
        self.list_of_games = QWidget()
        self.setup_list_of_games()

        self.tab_widget.addTab(self.home, "Home")
        self.tab_widget.addTab(self.euchre, "Euchre")
        self.tab_widget.addTab(self.hearts, "Hearts")
        self.tab_widget.addTab(self.list_of_games, "List Of Games")

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.tab_widget)

        default_width = 800
        default_height = 600
        self.resize(default_width, default_height)

    def setup_home(self):
        layout = QVBoxLayout(self.home)
        
        # Load the image
        pixmap = QPixmap("GameGenie\genie_logo.png")  # Replace "path_to_your_image_file.jpg" with the actual path to your image file
        if not pixmap.isNull():  # Check if the image loaded successfully
            # Create a QLabel to display the image
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)
        else:
            # If the image failed to load, display an error message
            error_label = QLabel("Failed to load image.")
            layout.addWidget(error_label)

        button = QPushButton("Start Playing")
        button.clicked.connect(lambda: self.tab_widget.setCurrentIndex(3))
        layout.addWidget(button)

    def setup_euchre(self):
        names_array = ["Player"]
        print_array = [QLabel("Names: Player")]
        result_label = QLabel("Tournament Result: ")  # New result_label
        table = EuchreTable(names_array, print_array, result_label)

        layout = QVBoxLayout(self.euchre)
        layout.addWidget(table)
        add_name_button = QPushButton("Add Name")
        add_name_button.clicked.connect(table.add_name_button_clicked)
        add_funk_button = QPushButton("Create Tournament")
        add_funk_button.clicked.connect(lambda: self.run_tournament(table))
        layout.addWidget(add_name_button)
        layout.addWidget(add_funk_button)
        layout.addWidget(print_array[0])
        layout.addWidget(result_label)

    def setup_hearts(self):
        data = [[0, 0, 0, 0]]

        result_labels = [QLabel(f"Player {i + 1} Score: 0") for i in range(4)]
        passing_order = passing[1 % len(passing)]
        passing_label = QLabel(f"Passing Order: {passing_order}")

        table = HeartsTable(data, result_labels, passing_label)

        layout = QVBoxLayout(self.hearts)
        layout.addWidget(passing_label)  # Add the passing order label
        layout.addWidget(table)

        for label in result_labels:
            layout.addWidget(label)
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

    def run_tournament(self, table):
        result = create_tournament(names=table.names_array)
        table.result_label.setText(f"Tournament Bracket:\n {result}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    style_file = QFile("GameGenie/style.qss")
    if style_file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(style_file)
        app.setStyleSheet(stream.readAll())
        style_file.close()

    window.show()
    sys.exit(app.exec_())
