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

    def __init__(self, pinsx, pinsy, pumper_pin1, pumper_pin2, motor_pin_enable):
        self.filename = ""
        #self.delay = 0.002
        self.pinsx = pinsx
        self.pinsy = pinsy
        self.motor_pin_enable = motor_pin_enable

        self.pumper_pin1 = pumper_pin1
        self.pumper_pin2 = pumper_pin2

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

        self.motor_delay = self.getCurrentMotorDelayFromSlider()

        self.sliderPumper.setMinimum(1)  # 0.05
        self.sliderPumper.setMaximum(10) # 0.5
        self.sliderPumper.setSingleStep(1)
        self.sliderPumper.setValue(10)    # 0.25

        self.pumper_speed = self.getCurrentPumperSpeedFromSlider()

        self.checkFileName(self.filename)

        self.pancake_machine = PancakeMachine(self.pinsx, self.pinsy, self.motor_delay, self.pumper_pin1, self.pumper_pin2, self.pumper_speed, 0.5, self.motor_pin_enable)
        self.pancake_printer = PancakePrintThread(self.filename, self.pancake_machine)
        self.pancake_test = PumperTestThread(self.pancake_machine)


    # ui part
    def isStartClicked(self):
        return self.btnStartEnd.isChecked()

    def resetStartEndButton(self):
        self.btnStartEnd.setChecked(False)
        _translate = QtCore.QCoreApplication.translate
        self.btnStartEnd.setText(_translate("MainWindow", "Start"))

    def checkFileName(self, filename):
        self.btnStartEnd.setEnabled(bool(filename))
        self.edtFilePath.setText(filename)
        self.sliderSpeed.setEnabled(bool(filename))

    def getCurrentMotorDelayFromSlider(self):
        delay = (11 - self.sliderSpeed.value()) / 1000.0
        return delay

    def isPumperTestClicked(self):
        return self.btnTest.isChecked()

    def resetartPumperTestButton(self):
        self.btnTest.setChecked(False)

    def getCurrentPumperSpeedFromSlider(self):
        speed = self.sliderPumper.value() / 20.0
        return speed

    # response to the ui event
    def pressedStartEndButton(self):
        _translate = QtCore.QCoreApplication.translate
        if self.isStartClicked():
            print("Start!")
            self.btnStartEnd.setText(_translate("MainWindow", "Stop"))
            self.pancake_printer = PancakePrintThread(self.filename, self.pancake_machine)
            self.pancake_printer.pancake_printed.connect(self.onPancakePrinted)
            self.pancake_printer.start()

            self.pancake_test.start()
        else:
            print("Stop!")
            self.btnStartEnd.setText(_translate("MainWindow", "Start"))
            self.pancake_machine.stop()

            self.pancake_machine.stopTestPumper()

    def sliderSpeedReleased(self):
        delay = self.getCurrentMotorDelayFromSlider()
        if delay != self.motor_delay:
            self.motor_delay = delay
            self.pancake_machine.changeMotorDelay(self.motor_delay)

    def pressedBrowseButton(self):
        self.filename, _ = QFileDialog.getOpenFileName(None, "Open File", "/home/pi/Sync", "gcode file (*.gcode)")
        self.checkFileName(self.filename)


    def closeEvent(self, event):
        print("User has clicked the red x on the main window")
        self.pancake_machine.stop()
        self.pancake_machine.stopTestPumper()
            
        self.pancake_printer.wait()
        self.pancake_test.wait()
            
        event.accept()

    def onPancakePrinted(self):
        print("Finished")
        self.pancake_machine.stopTestPumper()
        self.resetStartEndButton()

    def pressedPumperTestButton(self):
        if self.isPumperTestClicked():
            print("Test!")
            self.pancake_test.start()
        else:
            print("Stop!")
            self.pancake_machine.stopTestPumper()

    def sliderPumperSpeedReleased(self):
        speed = self.getCurrentPumperSpeedFromSlider()
        if speed != self.pumper_speed:
            self.pumper_speed = speed
            self.pancake_machine.changePumperSpeed(self.pumper_speed)