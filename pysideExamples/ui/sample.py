# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Solo(object):
    def setupUi(self, Solo):
        Solo.setObjectName("Solo")
        Solo.resize(979, 615)
        self.buttonBox = QtWidgets.QDialogButtonBox(Solo)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(Solo)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Solo)
        self.label.setGeometry(QtCore.QRect(50, 240, 55, 16))
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Solo)
        self.progressBar.setGeometry(QtCore.QRect(120, 560, 651, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Solo)
        self.textBrowser_2.setGeometry(QtCore.QRect(610, 20, 256, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(Solo)
        self.calendarWidget.setGeometry(QtCore.QRect(470, 240, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(Solo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 339, 371, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.dockWidget = QtWidgets.QDockWidget(Solo)
        self.dockWidget.setGeometry(QtCore.QRect(410, 80, 120, 80))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.checkBox = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(20, 10, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.dockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(Solo)
        self.buttonBox.accepted.connect(Solo.accept) # type: ignore
        self.buttonBox.rejected.connect(Solo.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Solo)

    def retranslateUi(self, Solo):
        _translate = QtCore.QCoreApplication.translate
        Solo.setWindowTitle(_translate("Solo", "Dialog"))
        self.buttonBox.setToolTip(_translate("Solo", "<html><head/><body><p>Click here</p></body></html>"))
        self.textBrowser.setHtml(_translate("Solo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Omni Text</p></body></html>"))
        self.label.setText(_translate("Solo", "Factoring"))
        self.textBrowser_2.setHtml(_translate("Solo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Coda one thing</p></body></html>"))
        self.pushButton_2.setText(_translate("Solo", "PushButton"))
        self.pushButton.setText(_translate("Solo", "PushButton"))
        self.checkBox.setText(_translate("Solo", "CheckBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Solo = QtWidgets.QDialog()
    ui = Ui_Solo()
    ui.setupUi(Solo)
    Solo.show()
    sys.exit(app.exec_())
