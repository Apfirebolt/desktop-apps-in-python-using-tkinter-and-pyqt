import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QMessageBox, QFrame)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        self.messageBox = QMessageBox()
        self.messageBox.setText("The document has been modified.");
        self.frame = QFrame()
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(3)
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setFrameShadow(QFrame.Plain)
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.messageBox)
        layout.addWidget(self.frame)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        print ("Hello %s" % self.edit.text())

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())