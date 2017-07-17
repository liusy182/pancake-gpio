from __future__ import absolute_import

import sys
import os
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import ui_mainwindow
from pancakemachine import PancakeMachine

class PancakePrintThread(QtCore.QThread):

    pancake_printed = QtCore.pyqtSignal()

    def __init__(self, filename, pancake_machine):
        QtCore.QThread.__init__(self)
        self.filename = filename
        self.pancake_machine = pancake_machine

    def run(self):
        if self.pancake_machine.start(self.filename):
            self.pancake_printed.emit()
    
class PumperTestThread(QtCore.QThread):

    def __init__(self, pancake_machine):
        QtCore.QThread.__init__(self)
        self.pancake_machine = pancake_machine

    def run(self):
        self.pancake_machine.testPumper()

class MainWindow(QMainWindow, ui_mainwindow.Ui_MainWindow):

    def __init__(self, pinsx, pinsy, pumper_pin):
        self.filename = ""
        self.delay = 0.002
        self.pinsx = pinsx
        self.pinsy = pinsy

        self.pumper_pin = pumper_pin
        self.pumper_speed = 0.25
        self.pancake_machine = PancakeMachine(self.pinsx, self.pinsy, self.delay, self.pumper_pin, self.pumper_speed)

        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        self.btnStartEnd.clicked.connect(lambda: self.pressedStartEndButton())
        self.btnBrowse.clicked.connect(lambda: self.pressedBrowseButton())
        self.sliderSpeed.sliderReleased.connect(lambda: self.sliderSpeedReleased())

        self.btnTest.clicked.connect(lambda: self.pressedPumperTestButton())
        self.sliderPumper.sliderReleased.connect(lambda: self.sliderPumperSpeedReleased())

        self.resetStartEndButton()

        self.sliderSpeed.setMinimum(1)  # 0.01
        self.sliderSpeed.setMaximum(10) # 0.001
        self.sliderSpeed.setSingleStep(1)
        self.sliderSpeed.setValue(9)    # 0.005

        self.getCurrentDelayFromSlider()

        self.sliderPumper.setMinimum(1)  # 0.05
        self.sliderPumper.setMaximum(10) # 0.5
        self.sliderPumper.setSingleStep(1)
        self.sliderPumper.setValue(5)    # 0.25

        self.getCurrentPumperSpeedFromSlider()


        self.checkFileName()


    def isStartClicked(self):
        return self.btnStartEnd.isChecked()

    def resetStartEndButton(self):
        self.btnStartEnd.setChecked(False)
        _translate = QtCore.QCoreApplication.translate
        self.btnStartEnd.setText(_translate("MainWindow", "Start"))

    def checkFileName(self):
        self.btnStartEnd.setEnabled(bool(self.filename))
        self.edtFilePath.setText(self.filename)
        self.sliderSpeed.setEnabled(bool(self.filename))

    def getCurrentDelayFromSlider(self):
        delay = (11 - self.sliderSpeed.value()) / 1000.0
        if delay != self.delay:
            self.delay = delay
            return True
        return False

    def pressedStartEndButton(self):
        _translate = QtCore.QCoreApplication.translate
        if self.isStartClicked():
            print("Start!")
            self.btnStartEnd.setText(_translate("MainWindow", "Stop"))
            
            self.pancake_printer = PancakePrintThread(self.filename, self.pancake_machine)
            self.pancake_printer.pancake_printed.connect(self.onPancakePrinted)
            self.pancake_printer.start()
        else:
            print("Stop!")
            self.btnStartEnd.setText(_translate("MainWindow", "Start"))
            self.pancake_machine.stop()

    def sliderSpeedReleased(self):
        if self.getCurrentDelayFromSlider():
            self.pancake_machine.changeDelay(self.delay)

    def pressedBrowseButton(self):
        self.filename, _ = QFileDialog.getOpenFileName(None, "Open File", "/home/pi/sync", "gcode file (*.gcode)")
        self.checkFileName()


    def closeEvent(self, event):
        print("User has clicked the red x on the main window")
        if not self.pancake_machine is None:
            self.pancake_machine.stop()
        event.accept()

    def onPancakePrinted(self):
        print("Finished")
        self.resetStartEndButton()

    def isPumperTestClicked(self):
        return self.btnTest.isChecked()

    def resetartPumperTestButton(self):
        self.btnTest.setChecked(False)

    def getCurrentPumperSpeedFromSlider(self):
        speed = self.sliderPumper.value() / 20.0
        if speed != self.pumper_speed:
            self.pumper_speed = speed
            return True
        return False

    def pressedPumperTestButton(self):
        if self.isPumperTestClicked():
            print("Test!")
            
            self.pancake_test = PumperTestThread(self.pancake_machine)
            self.pancake_test.start()
        else:
            print("Stop!")
            self.pancake_machine.stopTestPumper()

    def sliderPumperSpeedReleased(self):
        if self.getCurrentPumperSpeedFromSlider():
            self.pancake_machine.changePumperSpeed(self.pumper_speed)