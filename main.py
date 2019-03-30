
import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.LoadLocalDataButton.clicked.connect(self.onPushButtonClick)
        self.show()

    def onPushButtonClick(self):
        import os
        directory = os.getcwd()


        fname = QFileDialog.getOpenFileNames(self, 'Open file', directory)
        print(fname[0])
        self.chosenFiles = fname[0]
    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dl = MainWindow()
    sys.exit(app.exec_())