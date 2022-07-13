import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QApplication, QFrame, QWidget, QVBoxLayout


class HLine(QFrame):
    def __init__(self, parent=None, color=QColor("black")):
        super(HLine, self).__init__(parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(0)
        self.setMidLineWidth(3)
        self.setContentsMargins(0, 0, 0, 0)
        self.setColor(color)

    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 400)
    lay = QVBoxLayout(w)
    lay.addWidget(HLine())

    for color in [QColor("red"), QColor(0, 255, 0), QColor(Qt.blue)]:
        h = HLine()
        h.setColor(color)
        lay.addWidget(h)

    w.show()
    sys.exit(app.exec_())