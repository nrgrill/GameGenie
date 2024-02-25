import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, QFile, QTextStream

#See this thing creates the table silly
class MyTable(QTableWidget):
    def __init__(self, data, result_labels):
        super().__init__()
        self.result_labels = result_labels
        self.setRowCount(len(data))
        self.setColumnCount(len(data[0]))
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                item_widget = QTableWidgetItem(str(item))
                item_widget.setFlags(item_widget.flags() | Qt.ItemFlag.ItemIsEditable)
                self.setItem(i, j, item_widget)
        self.itemChanged.connect(self.update_totals)

    #See this thing adds the stuff from the table to the total thing so you can see the total on the app of course on god
    def update_totals(self, item):
        total = 0
        column_index = item.column()
        for i in range(self.rowCount()):
            try:
                total += int(self.item(i, column_index).text())
            except ValueError:
                pass
        self.result_labels[column_index].setText(f"player {column_index + 1} Score: {total}")

    #Does what it says obviously
    def add_row_button_clicked(self):
        current_row_count = self.rowCount()
        self.insertRow(current_row_count)
        #Creates the array thang
        for j in range(self.columnCount()):
            item_widget = QTableWidgetItem("0")
            item_widget.setFlags(item_widget.flags() | Qt.ItemFlag.ItemIsEditable)
            self.setItem(current_row_count, j, item_widget)

        # Updates totals after the new row is made for sure ong god no cap
        for column_index in range(self.columnCount()):
            self.update_totals(self.item(current_row_count, column_index))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.tab_widget = QTabWidget(self.central_widget)

        #this thing like, Uh, It adds the page ya that is what it does
        self.home = QWidget()
        self.setup_home()
        self.euchre = QWidget()
        self.setup_euchre()
        self.Hearts = QWidget()
        self.setup_hearts()
        self.list_of_games = QWidget()
        self.setup_list_of_games()

        #Adds the tabs to the thing i think orsomethin
        self.tab_widget.addTab(self.home, "Home")
        self.tab_widget.addTab(self.euchre, "Euchre")
        self.tab_widget.addTab(self.Hearts, "Hearts")
        self.tab_widget.addTab(self.list_of_games, "List Of Games")

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.tab_widget)

        #How to change thy app size ya dingy
        default_width = 800
        default_height = 600
        self.resize(default_width, default_height)

    def setup_home(self):
        label = QLabel("CUM")
        layout = QVBoxLayout(self.home)
        layout.addWidget(label)
        button = QPushButton("Start Playing")
        button.clicked.connect(lambda: self.tab_widget.setCurrentIndex(3))
        layout.addWidget(button)

    #This is where the dumbys will format their tab
    def setup_euchre(self):
        label = QLabel("Content of Page 1")
        layout = QVBoxLayout(self.euchre)
        layout.addWidget(label)

    #Made this with my dick and balls
    def setup_hearts(self):
        data = [[0, 0, 0, 0]]
        result_labels = [QLabel(f"Total for Column {i + 1}: 0") for i in range(4)]
        table = MyTable(data, result_labels)

        layout = QVBoxLayout(self.Hearts)
        layout.addWidget(table)

        for label in result_labels:
            layout.addWidget(label)
        add_row_button = QPushButton("Add Row")
        add_row_button.clicked.connect(table.add_row_button_clicked)
        layout.addWidget(add_row_button)

    #where we do the thing to do the thing to tell the description before playing the thing ya
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


#Runs the thing or something idfk
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    #imports the style sheet for the colors CUH
    style_file = QFile("GameGenie\style.qss")
    if style_file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(style_file)
        app.setStyleSheet(stream.readAll())
        style_file.close()

    window.show()
    sys.exit(app.exec_())
