import sys
from time import sleep

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QWidget,
    QHBoxLayout
)


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicksCount = 0
        self.setupUi()

    def setupUi(self):
        self.clicksLabel = QLabel("Counting: 0 clicks", self)
        self.setWindowTitle('A new widget of stars')
        self.resize(300, 400)
        self.clicksLabel.setAlignment(Qt.AlignHCenter or Qt.AlignVCenter)        
    

    
app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())