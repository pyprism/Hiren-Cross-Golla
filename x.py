from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import main

class Hiren(QMainWindow, main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Hiren, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
form = Hiren()
form.show()
app.exec_()
