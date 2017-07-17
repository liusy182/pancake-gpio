from __future__ import absolute_import

import sys
import os
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import ui_mainwindow
from pancakemachine_mock import PancakeMachine

class PancakePrintThread(QtCore.QThread):

    pancake_printed = QtCore.pyqtSignal()

    def __init__(self, filename, pancake_machine):
        QtCore.QThread.__init__(self)
        self.filename = filename
        self.pancake_machine = pancake_machine

    def run(self):
        if self.pancake_machine.start(self.filename):
            self.pancake_printed.emit()

class MainWindow(QMainWindow, ui_mainwindow.Ui_MainWindow):

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

            self.pancake_machine = PancakeMachine(self.pinsx, self.pinsy, self.delay)
            
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
        self.filename, _ = QFileDialog.getOpenFileName(None, "Open File", os.getcwd(), "gcode file (*.gcode)")
        self.checkFileName()

    def __init__(self, pinsx, pinsy):
        self.filename = ""
        self.delay = 0.0005
        self.pinsx = pinsx
        self.pinsy = pinsy
        self.pancake_machine = None

        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        self.btnStartEnd.clicked.connect(lambda: self.pressedStartEndButton())
        self.btnBrowse.clicked.connect(lambda: self.pressedBrowseButton())
        self.sliderSpeed.sliderReleased.connect(lambda: self.sliderSpeedReleased())

        self.resetStartEndButton()

        self.sliderSpeed.setMinimum(1)  # 0.01
        self.sliderSpeed.setMaximum(10) # 0.001
        self.sliderSpeed.setSingleStep(1)
        self.sliderSpeed.setValue(6)    # 0.005

        self.getCurrentDelayFromSlider()

        self.checkFileName()


    def closeEvent(self, event):
        print("User has clicked the red x on the main window")
        if not self.pancake_machine is None:
            self.pancake_machine.stop()
        event.accept()

    def onPancakePrinted(self):
        print("Finished")
        self.resetStartEndButton()