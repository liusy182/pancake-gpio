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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wgtTop = QtWidgets.QWidget(self.centralWidget)
        self.wgtTop.setObjectName("wgtTop")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wgtTop)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edtFilePath = QtWidgets.QLineEdit(self.wgtTop)
        self.edtFilePath.setText("")
        self.edtFilePath.setObjectName("edtFilePath")
        self.horizontalLayout.addWidget(self.edtFilePath)
        self.btnBrowse = QtWidgets.QPushButton(self.wgtTop)
        self.btnBrowse.setEnabled(True)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.verticalLayout.addWidget(self.wgtTop)
        self.wgtBottom = QtWidgets.QWidget(self.centralWidget)
        self.wgtBottom.setObjectName("wgtBottom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wgtBottom)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnStartEnd = QtWidgets.QPushButton(self.wgtBottom)
        self.btnStartEnd.setCheckable(True)
        self.btnStartEnd.setObjectName("btnStartEnd")
        self.horizontalLayout_2.addWidget(self.btnStartEnd)
        self.btnOn = QtWidgets.QPushButton(self.wgtBottom)
        self.btnOn.setObjectName("btnOn")
        self.horizontalLayout_2.addWidget(self.btnOn)
        self.btnOff = QtWidgets.QPushButton(self.wgtBottom)
        self.btnOff.setObjectName("btnOff")
        self.horizontalLayout_2.addWidget(self.btnOff)
        self.verticalLayout.addWidget(self.wgtBottom)
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
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.btnStartEnd.setText(_translate("MainWindow", "Start"))
        self.btnOn.setText(_translate("MainWindow", "+"))
        self.btnOff.setText(_translate("MainWindow", "-"))

