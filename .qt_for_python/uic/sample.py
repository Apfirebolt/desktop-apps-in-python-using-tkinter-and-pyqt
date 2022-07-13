# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sample.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Solo(object):
    def setupUi(self, Solo):
        if not Solo.objectName():
            Solo.setObjectName(u"Solo")
        Solo.resize(979, 615)
        self.buttonBox = QDialogButtonBox(Solo)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.textBrowser = QTextBrowser(Solo)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 20, 256, 192))
        self.label = QLabel(Solo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 240, 55, 16))
        self.label.setAutoFillBackground(True)
        self.progressBar = QProgressBar(Solo)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(120, 560, 651, 23))
        self.progressBar.setValue(24)
        self.textBrowser_2 = QTextBrowser(Solo)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(610, 20, 256, 192))
        self.calendarWidget = QCalendarWidget(Solo)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(470, 240, 392, 236))
        self.verticalLayoutWidget = QWidget(Solo)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 339, 371, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(85, 255, 127);")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.dockWidget = QDockWidget(Solo)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setGeometry(QRect(410, 80, 120, 80))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.checkBox = QCheckBox(self.dockWidgetContents)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 10, 81, 20))
        self.dockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(Solo)
        self.buttonBox.accepted.connect(Solo.accept)
        self.buttonBox.rejected.connect(Solo.reject)

        QMetaObject.connectSlotsByName(Solo)
    # setupUi

    def retranslateUi(self, Solo):
        Solo.setWindowTitle(QCoreApplication.translate("Solo", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.buttonBox.setToolTip(QCoreApplication.translate("Solo", u"<html><head/><body><p>Click here</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.textBrowser.setHtml(QCoreApplication.translate("Solo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Omni Text</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Solo", u"Factoring", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Solo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Coda one thing</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Solo", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Solo", u"PushButton", None))
        self.checkBox.setText(QCoreApplication.translate("Solo", u"CheckBox", None))
    # retranslateUi

