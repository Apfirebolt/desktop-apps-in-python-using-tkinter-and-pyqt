import sys
from PySide2 import QtWidgets, QtScript


app = QtWidgets.QApplication(sys.argv)

engine = QtScript.QScriptEngine()

button = QtWidgets.QPushButton()
scriptButton = engine.newQObject(button)
engine.globalObject().setProperty("button", scriptButton)

engine.evaluate("button.text = 'Hello World from PySide2!'")
engine.evaluate("button.styleSheet = 'font-style: italic'")
engine.evaluate("button.show()")

sys.exit(app.exec_())