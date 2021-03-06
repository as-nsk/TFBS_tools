# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(120, 10, 561, 201))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 314, 61, 16))
        self.label.setObjectName("label")
        self.LoadLocalDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadLocalDataButton.setGeometry(QtCore.QRect(119, 275, 221, 23))
        self.LoadLocalDataButton.setObjectName("LoadLocalDataButton")
        self.OpenFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFolderButton.setGeometry(QtCore.QRect(490, 230, 61, 21))
        self.OpenFolderButton.setObjectName("OpenFolderButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(118, 314, 141, 21))
        self.label_3.setObjectName("label_3")
        self.AboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.AboutButton.setGeometry(QtCore.QRect(30, 534, 75, 23))
        self.AboutButton.setObjectName("AboutButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(118, 248, 61, 16))
        self.label_4.setObjectName("label_4")
        self.LoadDataFromGencodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadDataFromGencodeButton.setGeometry(QtCore.QRect(350, 275, 171, 23))
        self.LoadDataFromGencodeButton.setObjectName("LoadDataFromGencodeButton")
        self.BuildClustersButton = QtWidgets.QPushButton(self.centralwidget)
        self.BuildClustersButton.setGeometry(QtCore.QRect(118, 334, 221, 23))
        self.BuildClustersButton.setObjectName("BuildClustersButton")
        self.GetChIPseqPeakProfilesButto = QtWidgets.QPushButton(self.centralwidget)
        self.GetChIPseqPeakProfilesButto.setGeometry(QtCore.QRect(116, 495, 231, 21))
        self.GetChIPseqPeakProfilesButto.setObjectName("GetChIPseqPeakProfilesButto")
        self.CountNumberOfIntersectionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.CountNumberOfIntersectionsButton.setGeometry(QtCore.QRect(117, 366, 221, 23))
        self.CountNumberOfIntersectionsButton.setObjectName("CountNumberOfIntersectionsButton")
        self.ChangeFolderButton = QtWidgets.QToolButton(self.centralwidget)
        self.ChangeFolderButton.setGeometry(QtCore.QRect(440, 231, 31, 20))
        self.ChangeFolderButton.setObjectName("ChangeFolderButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(352, 229, 81, 21))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 230, 61, 16))
        self.label_2.setObjectName("label_2")
        self.BuildClustersProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.BuildClustersProgressBar.setGeometry(QtCore.QRect(590, 337, 101, 16))
        self.BuildClustersProgressBar.setProperty("value", 24)
        self.BuildClustersProgressBar.setObjectName("progressBar")
        self.CountNumberOfIntersectionsProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.CountNumberOfIntersectionsProgressBar.setGeometry(QtCore.QRect(590, 368, 101, 16))
        self.CountNumberOfIntersectionsProgressBar.setProperty("value", 24)
        self.CountNumberOfIntersectionsProgressBar.setObjectName("CountNumberOfIntersectionsProgressBar")
        self.ExportHistogramsProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ExportHistogramsProgressBar.setGeometry(QtCore.QRect(590, 447, 101, 16))
        self.ExportHistogramsProgressBar.setProperty("value", 24)
        self.ExportHistogramsProgressBar.setObjectName("ExportHistogramsProgressBar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 414, 141, 21))
        self.label_5.setObjectName("label_5")
        self.BuildHistogramsButton = QtWidgets.QPushButton(self.centralwidget)
        self.BuildHistogramsButton.setGeometry(QtCore.QRect(118, 444, 231, 21))
        self.BuildHistogramsButton.setObjectName("BuildHistogramsButton")
        self.BuildHeatmapsButton = QtWidgets.QPushButton(self.centralwidget)
        self.BuildHeatmapsButton.setGeometry(QtCore.QRect(117, 470, 231, 21))
        self.BuildHeatmapsButton.setObjectName("BuildHeatmapsButton")
        self.ExportHeatmapsProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ExportHeatmapsProgressBar.setGeometry(QtCore.QRect(590, 473, 101, 16))
        self.ExportHeatmapsProgressBar.setProperty("value", 24)
        self.ExportHeatmapsProgressBar.setObjectName("ExportHeatmapsProgressBar")
        self.ExportChIPseqPeakProfilesProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ExportChIPseqPeakProfilesProgressBar.setGeometry(QtCore.QRect(590, 497, 101, 16))
        self.ExportChIPseqPeakProfilesProgressBar.setProperty("value", 24)
        self.ExportChIPseqPeakProfilesProgressBar.setObjectName("ExportChIPseqPeakProfilesProgressBar")
        self.LoadDataProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.LoadDataProgressBar.setGeometry(QtCore.QRect(590, 278, 101, 16))
        self.LoadDataProgressBar.setProperty("value", 24)
        self.LoadDataProgressBar.setObjectName("LoadDataProgressBar")
        self.HelpButton = QtWidgets.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(690, 534, 75, 23))
        self.HelpButton.setObjectName("HelpButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 334, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(460, 334, 71, 21))
        self.label_8.setObjectName("label_8")
        self.MergeGap = QtWidgets.QLineEdit(self.centralwidget)
        self.MergeGap.setGeometry(QtCore.QRect(420, 334, 31, 20))
        self.MergeGap.setObjectName("MergeGap")
        self.MaxLength = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxLength.setGeometry(QtCore.QRect(520, 334, 31, 20))
        self.MaxLength.setObjectName("MaxLength")
        self.ExportHistogramsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ExportHistogramsCheckBox.setGeometry(QtCore.QRect(370, 444, 191, 17))
        self.ExportHistogramsCheckBox.setObjectName("checkBox")
        self.ExportHeatmapsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ExportHeatmapsCheckBox.setGeometry(QtCore.QRect(370, 459, 191, 40))
        self.ExportHeatmapsCheckBox.setObjectName("ExportHeatmapsCheckBox")
        self.ExportChIPseqPeakProfilesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ExportChIPseqPeakProfilesCheckBox.setGeometry(QtCore.QRect(370, 490, 191, 30))
        self.ExportChIPseqPeakProfilesCheckBox.setObjectName("ExportChIPseqPeakProfilesCheckBox")
        self.ShuffleDataCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ShuffleDataCheckBox.setGeometry(QtCore.QRect(371, 370, 101, 17))
        self.ShuffleDataCheckBox.setObjectName("ShuffleDataCheckBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Parametres"))
        self.LoadLocalDataButton.setText(_translate("MainWindow", "Load local data from the working folder"))
        self.OpenFolderButton.setText(_translate("MainWindow", "Open "))
        self.label_3.setText(_translate("MainWindow", "Procedures"))
        self.AboutButton.setText(_translate("MainWindow", "About"))
        self.label_4.setText(_translate("MainWindow", "Input"))
        self.LoadDataFromGencodeButton.setText(_translate("MainWindow", "Load BED data from GENCODE"))
        self.BuildClustersButton.setText(_translate("MainWindow", "Build clusters"))
        self.GetChIPseqPeakProfilesButto.setText(_translate("MainWindow", "Show ChIP-seq-peak profiles from UCSC"))
        self.CountNumberOfIntersectionsButton.setText(_translate("MainWindow", "Count the number of paired intersections"))
        self.ChangeFolderButton.setText(_translate("MainWindow", "..."))
        self.label_6.setText(_translate("MainWindow", "Working folder:"))
        self.label_2.setText(_translate("MainWindow", "Progress"))
        self.label_5.setText(_translate("MainWindow", "Output"))
        self.BuildHistogramsButton.setText(_translate("MainWindow", "Build the histograms for the chosen TF set"))
        self.BuildHeatmapsButton.setText(_translate("MainWindow", "Build the heatmaps for the chosen TF set"))
        self.HelpButton.setText(_translate("MainWindow", "Help"))
        self.label_7.setText(_translate("MainWindow", "Merge gap:"))
        self.label_8.setText(_translate("MainWindow", "Max length:"))
        self.ExportHistogramsCheckBox.setText(_translate("MainWindow", "Export to the working directory"))
        self.ExportHeatmapsCheckBox.setText(_translate("MainWindow", "Export to the working directory"))
        self.ExportChIPseqPeakProfilesCheckBox.setText(_translate("MainWindow", "Export to the working directory"))
        self.ShuffleDataCheckBox.setText(_translate("MainWindow", "Shuffle data"))


