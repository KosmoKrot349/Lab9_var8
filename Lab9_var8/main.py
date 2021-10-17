import sys
from LogInWindow import *
from MainWindow import *
from CustomDbContext import *
from PyQt5.QtWidgets import *
if __name__ =='__main__':
    app = QApplication(sys.argv)
    context=DbContext()
    mainWind=MainWindow()
    ex = LogInWindow(context,mainWind)
    sys.exit(app.exec_())
