import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel("A new label of the text")

        


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()