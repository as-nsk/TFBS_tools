import os
import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
import Buildclusters
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QLineEdit,
    QAction, QFileDialog, QApplication)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.LoadLocalDataButton.clicked.connect(self.onPushButtonClick)
        self.ui.BuildClustersButton.clicked.connect(self.BuildClustersClick)
        self.ui.MergeGap.setText('200')
        self.ui.MaxLength.setText('500')
        self.show()

        self.chosen_files = []

    def onPushButtonClick(self):
        print("test")

        directory = os.getcwd()

        fname = QFileDialog.getOpenFileNames(self, 'Open file', directory)
        # print(fname[0])
        self.chosen_files = fname[0]

    def BuildClustersClick(self):
        merge_gap = self.ui.MergeGap.text()
        try:
            merge_gap = int(merge_gap)
        except:
            pass
            print('merge_gap is not valid integer')
            return
            # TODO: show error message box

        max_length = self.ui.MaxLength.text()
        try:
            max_length = int(max_length)
        except:
            # TODO: show error message box
            print('max_length is not valid integer')
            return

        print(merge_gap)
        print('here we will build clusters')
        if self.chosen_files:
            print(self.chosen_files)
            intervals = Buildclusters.build(self.chosen_files, merge_gap, max_length)
            pass
        else:
            print('no files were chosen')




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dl = MainWindow()
    sys.exit(app.exec_())