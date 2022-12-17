import pandas as pd
import operator
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore


class MyWindow(QtWidgets.QWidget):
    def __init__(self, data_list, header, *args):
        QtWidgets.QWidget.__init__(self, *args)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 200, 970, 650)
        self.setWindowTitle("Click on column title to sort")
        table_model = MyTableModel(self, data_list, header)
        self.proxy_model = QtCore.QSortFilterProxyModel()
        self.proxy_model.setSourceModel(table_model)
        self.proxy_model.setFilterKeyColumn(0)
        self.table_view = QtWidgets.QTableView()
        self.table_view.clicked.connect(self.table_clicked)
        self.table_view.setModel(table_model)
        # set font
        font = QtGui.QFont("Courier New", 14)
        self.table_view.setFont(font)
        # set column width to fit contents (set font first!)
        self.table_view.resizeColumnsToContents()

        header = self.table_view.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)


        # enable sorting
        self.table_view.setSortingEnabled(True)
        self.table_view.setModel(self.proxy_model)
        searchFilter = QtWidgets.QLineEdit()
        searchFilter.textChanged.connect(self.update_search)
        filterLabel = QtWidgets.QLabel('Search Filter')
        filterColumnSelectLabel = QtWidgets.QLabel('Select Filter')
        filterLayout = QtWidgets.QHBoxLayout()
        filterLayout.addWidget(filterLabel)
        filterLayout.addWidget(searchFilter)
        filterLayout.addWidget(filterColumnSelectLabel)

        # Combo box for filtering
        filterComboBox = QtWidgets.QComboBox(self)
        columnNames = ["Car Name", "Year", "Selling Price"]
        filterComboBox.addItems(columnNames)
  
        # item
        item ="Car Name"
        filterComboBox.setCurrentText(item)
        filterComboBox.currentTextChanged.connect(self.filter_changed)
        filterLayout.addWidget(filterComboBox)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(filterLayout)
        layout.addWidget(self.table_view)
        self.setLayout(layout)
    
    def update_search(self, text):
        self.proxy_model.setFilterWildcard('*%s*' % text)

    def filter_changed(self, text):
        if text == 'Car Name':
            self.proxy_model.setFilterKeyColumn(0)
        elif text == 'Year':
            self.proxy_model.setFilterKeyColumn(1)
        else:
            self.proxy_model.setFilterKeyColumn(2)

    
    def table_clicked(self):
        selected_indexes = self.table_view.selectionModel().selectedRows()
        print('Selected ', selected_indexes)


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
                             key=operator.itemgetter(col))
        if order == QtCore.Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))


df = pd.read_csv('cardata.csv')

header = list(df.columns)
data_list = list(df.itertuples(index=False, name=None))


app = QtWidgets.QApplication([])
win = MyWindow(data_list, header)
win.show()
app.exec_()