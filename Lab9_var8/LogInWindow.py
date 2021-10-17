import sys
from PyQt5.QtWidgets import *
from TableModel import *
from CustomDbContext import *
from MainWindow import *

class LogInWindow(QWidget):

    context = DbContext();

    def __init__(self,DbContext,mainWindow):
        self.context=DbContext
        self.mainWindow=mainWindow
        super().__init__()
        grid = QGridLayout()

        baseLabel = QLabel('База')
        userLabel = QLabel('Пользователь')
        passwordLabel = QLabel('Пароль')
        serverLabel = QLabel('Сервер')


        self.baseEdit = QLineEdit('dogs')
        self.userEdit = QLineEdit('root')
        self.passwordEdit = QLineEdit('1111')
        self.serverEdit = QLineEdit('localhost')
        self.btn = QPushButton('Подключиться')

        grid.addWidget(self.btn,5,0,1,2)
        self.btn.clicked.connect(self.buttonClicked)

        grid.addWidget(baseLabel, 1, 0)
        grid.addWidget(userLabel, 2, 0)
        grid.addWidget(passwordLabel, 3, 0)
        grid.addWidget(serverLabel, 4, 0)

        grid.addWidget(self.baseEdit, 1, 1)
        grid.addWidget(self.userEdit, 2, 1)
        grid.addWidget(self.passwordEdit, 3, 1)
        grid.addWidget(self.serverEdit, 4, 1)

        self.setLayout(grid)

        self.show()



    def buttonClicked(self):
        self.context.SetFileds(self.baseEdit.displayText(),self.userEdit.displayText(),self.passwordEdit.displayText(),self.serverEdit.displayText())
        self.context.CreateConnect()
        if self.context.isSuccessConnection==1:
            self.mainWindow.show()
            self.mainWindow.setContext(self.context)
            self.close()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Some errors happen")
            self.msg.exec_()





    