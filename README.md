![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)


# A collection of small desktop based apps in Python

Desktop apps such as calculator, clock and others in Python using Tkinter, PyQT5 and Pyside2.

## Getting Started

Create a new virtual environment as a best practice norm. Install python packages through pip using the bundled requirements
file. Tkinter already comes bundled with Python, but you'd need to install other similar alternatives used in this repository like PySide2 and PyQT5.

## QT Designer Tool for Pyside applications

There is a GUI drag and drop tool available for you in case you're using Pyside. The tool is called <strong>QT Designer</strong>. You can install this tool using the following command 

```
pip install pyqt5-tools
```

Inside your virtual environment site-packages folder you should 'designer.exe' file inside qt5_applications/Qt/bin directory. There is also an extension available to handle ui files if you're using Visual Studio Code. UI files need to be compiled into python files for Pyside which can be done using the following command in the terminal

```
pyuic5 -x new-ui.ui -o new-ui.py
```

Make sure you are inside the directory where your UI files reside.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


