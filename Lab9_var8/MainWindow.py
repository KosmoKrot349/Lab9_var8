import sys
from PyQt5.QtWidgets import *
from TableModel import *
from CustomDbContext import *

class MainWindow(QWidget):

    context = DbContext()

    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        idLabel = QLabel('Id')
        weightLabel = QLabel('Рост')
        heighLabel = QLabel('Вес')
        classificLabel = QLabel('Класс')
        foodLabel = QLabel('Еда')
        soundLabel = QLabel('Звуки издаёт')
        nameLabel = QLabel('Кличка')
        ageLabel = QLabel('Возраст')


        self.idEdit = QLineEdit()
        self.weightEdit = QLineEdit()
        self.heighEdit = QLineEdit()
        self.classificEdit = QLineEdit()
        self.foodEdit = QLineEdit()
        self.soundEdit = QLineEdit()
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()

        self.btn1 = QPushButton('Добавить')
        self.btn2 = QPushButton('Показать')
        self.btn3 = QPushButton('Удалить')
       
        self.table = QTableView()
        
        self.btn1.clicked.connect(self.AddClick)
        self.btn2.clicked.connect(self.ShowClick)
        self.btn3.clicked.connect(self.DelClick)

        grid.addWidget(self.table,1,1,8,1)

        grid.addWidget(idLabel, 1, 2)
        grid.addWidget(weightLabel, 2, 2)
        grid.addWidget(heighLabel, 3, 2)
        grid.addWidget(classificLabel, 4, 2)
        grid.addWidget(foodLabel, 5, 2)
        grid.addWidget(soundLabel, 6, 2)
        grid.addWidget(nameLabel, 7, 2)
        grid.addWidget(ageLabel, 8, 2)

        grid.addWidget(self.idEdit, 1, 3)
        grid.addWidget(self.weightEdit, 2, 3)
        grid.addWidget(self.heighEdit, 3, 3)
        grid.addWidget(self.classificEdit, 4, 3)
        grid.addWidget(self.foodEdit, 5, 3)
        grid.addWidget(self.soundEdit, 6, 3)
        grid.addWidget(self.nameEdit, 7, 3)
        grid.addWidget(self.ageEdit, 8, 3)

        grid.addWidget(self.btn1,9,1)
        grid.addWidget(self.btn2,9,2,)
        grid.addWidget(self.btn3,9,3,)

        self.setLayout(grid)

    def AddClick(self):
        self.context.ExecuteIntoDb(F'INSERT INTO dogs (weight,height,classification,sound,food,name,age)VALUES({self.weightEdit.displayText()},{self.heighEdit.displayText()},\'{self.classificEdit.displayText()}\',\'{self.foodEdit.displayText()}\',\'{self.soundEdit.displayText()}\',\'{self.nameEdit.displayText()}\',{self.ageEdit.displayText()})')
        self.ShowClick()

    def ShowClick(self):
        self.table.setModel(TableModel(self.context.ShowRecords('select * from dogs')))

    def DelClick(self):
        self.context.ExecuteIntoDb(F'delete from dogs where id={self.idEdit.displayText()}')
        self.ShowClick()

    def setContext(self,context):
        self.context=context
        





    