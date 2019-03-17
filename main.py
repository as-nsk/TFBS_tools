import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from tfbs_gui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dl = MainWindow()
    sys.exit(app.exec_())