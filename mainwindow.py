from __future__ import absolute_import

import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import ui_mainwindow
from pancakemachine_mock import PancakeMachine

class MainWindow(QMainWindow, ui_mainwindow.Ui_MainWindow):

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
            self.pancake_machine.stop()

    def pressedOnButton(self):
        if self.delay < self.max_delay:
            self.delay += self.delay_step
            self.pancake_machine.changeDelay(self.delay)
        print (self.delay)

    def pressedOffButton(self):
        if self.delay > self.min_delay:
            self.delay -= self.delay_step
            self.pancake_machine.changeDelay(self.delay)
        print (self.delay)

    def __init__(self, pinsx, pinsy):
        self.delay = 0.005
        self.max_delay = 0.01
        self.min_delay = 0
        self.delay_step = 0.001


        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        self.btnOn.clicked.connect(lambda: self.pressedOnButton())
        self.btnOff.clicked.connect(lambda: self.pressedOffButton())
        self.btnStartEnd.clicked.connect(lambda: self.pressedStartEndButton())

        self.pancake_machine = PancakeMachine(pinsx, pinsy, self.delay)

    def closeEvent(self, event):
        print("User has clicked the red x on the main window")
        self.pancake_machine.stop()
        event.accept()