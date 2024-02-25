import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Qt

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Add a label
        label = QLabel("Welcome to the Application")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        # Add buttons
        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button1_clicked)
        layout.addWidget(button1)
        
        button2 = QPushButton("Button 2")
        button2.clicked.connect(self.button2_clicked)
        layout.addWidget(button2)
        
    def button1_clicked(self):
        print("Button 1 clicked")
        # Add functionality for Button 1
        
    def button2_clicked(self):
        print("Button 2 clicked")
        # Add functionality for Button 2

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec())
