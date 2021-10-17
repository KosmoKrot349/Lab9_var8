import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    
    headers = ['id','wight','height','class','food','sound','name','age']
    headersData=headers
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
    
    #i hate this method 3:42 am
    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headersData[column]


