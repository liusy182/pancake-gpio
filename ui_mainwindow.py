# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnStartEnd = QtWidgets.QPushButton(self.centralWidget)
        self.btnStartEnd.setCheckable(True)
        self.btnStartEnd.setObjectName("btnStartEnd")
        self.horizontalLayout.addWidget(self.btnStartEnd)
        self.btnBrowse = QtWidgets.QPushButton(self.centralWidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.btnOn = QtWidgets.QPushButton(self.centralWidget)
        self.btnOn.setObjectName("btnOn")
        self.horizontalLayout.addWidget(self.btnOn)
        self.btnOff = QtWidgets.QPushButton(self.centralWidget)
        self.btnOff.setObjectName("btnOff")
        self.horizontalLayout.addWidget(self.btnOff)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pancake"))
        self.btnStartEnd.setText(_translate("MainWindow", "Start"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.btnOn.setText(_translate("MainWindow", "+"))
        self.btnOff.setText(_translate("MainWindow", "-"))

