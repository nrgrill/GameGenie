import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtCore import QFile, QTextStream

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.tab_widget = QTabWidget(self.central_widget)

        self.page1 = QWidget()
        self.setup_page1()

        self.page2 = QWidget()
        self.setup_page2()
        
        self.tab_widget.addTab(self.page1, "Page 1")
        self.tab_widget.addTab(self.page2, "Page 2")

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.tab_widget)
        
    def setup_page1(self):
        label = QLabel("Content of Page 1")
        button = QPushButton("Go to Page 2")
        button.clicked.connect(lambda: self.tab_widget.setCurrentIndex(1))

        layout = QVBoxLayout(self.page1)
        layout.addWidget(label)
        layout.addWidget(button)

    def setup_page2(self):
        label = QLabel("Content of Page 2")
        button = QPushButton("Go to Page 1")
        button.clicked.connect(lambda: self.tab_widget.setCurrentIndex(0))

        layout = QVBoxLayout(self.page2)
        layout.addWidget(label)
        layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    # Load and apply the style from style.qss
    style_file = QFile("GameGenie\style.qss")
    if style_file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(style_file)
        app.setStyleSheet(stream.readAll())
        style_file.close()

    window.show()
    sys.exit(app.exec_())
