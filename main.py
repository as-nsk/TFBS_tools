
import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.LoadLocalDataButton.clicked.connect(self.onPushButtonClick)
        self.show()

    def onPushButtonClick(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Select the files to be loaded")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Load local data")
        msg.setDetailedText("The details are as follows:")
        msg.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dl = MainWindow()
    sys.exit(app.exec_())