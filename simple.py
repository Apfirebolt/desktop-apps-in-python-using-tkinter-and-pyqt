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


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicksCount = 0
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Freezing GUI")
        self.resize(300, 150)
        # Create and connect widgets
        self.clicksLabel = QLabel("Counting: 0 clicks", self)
        self.clicksLabel.setAlignment(Qt.AlignHCenter or Qt.AlignVCenter)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.clickBtn = QPushButton('Drake')

        self.HLayout = QHBoxLayout()
        self.HLayout.addWidget(self.clickBtn)
        self.centralWidget.setLayout(self.HLayout)
        
    

    
app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())