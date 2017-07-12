from __future__ import absolute_import

import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import ui_mainwindow
from pancakemachine_mock import PancakeMachine

class MainWindow(QMainWindow, ui_mainwindow.Ui_MainWindow):

    current_value = 5
    max_value = 10
    min_value = 0
    value_step = 1

    def isStartClicked(self):
        return self.btnStartEnd.isChecked()

    def pressedStartEndButton(self):
        _translate = QtCore.QCoreApplication.translate
        if self.isStartClicked():
            print("Start!")
            self.btnStartEnd.setText(_translate("MainWindow", "Stop"))
            file = "sample.gcode"  # Change to get from Autodesk Cloud Storage later
            self.pancake_machine.start(file)
        else:
            print("Stop!")
            self.btnStartEnd.setText(_translate("MainWindow", "Start"))

    def pressedOnButton(self):
        if self.current_value < self.max_value:
            self.current_value += self.value_step
        print (self.current_value)

    def pressedOffButton(self):
        if self.current_value > self.min_value:
            self.current_value -= self.value_step
        print (self.current_value)

    def __init__(self, pinsx, pinsy):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        self.btnOn.clicked.connect(lambda: self.pressedOnButton())
        self.btnOff.clicked.connect(lambda: self.pressedOffButton())
        self.btnStartEnd.clicked.connect(lambda: self.pressedStartEndButton())

        self.pancake_machine = PancakeMachine(pinsx, pinsy)

