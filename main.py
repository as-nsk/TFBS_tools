import os
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
        self.ui.BuildClustersButton.clicked.connect(self.BuildClustersClick)
        self.show()

        self.chosen_files = []

    def onPushButtonClick(self):
        print("test")

        directory = os.getcwd()

        fname = QFileDialog.getOpenFileNames(self, 'Open file', directory)
        # print(fname[0])
        self.chosen_files = fname[0]

    def BuildClustersClick(self):
        print('here we will build clusters')
        if self.chosen_files:
            print(self.chosen_files)
        else:
            print('no files were chosen')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dl = MainWindow()
    sys.exit(app.exec_())