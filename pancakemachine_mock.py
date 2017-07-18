from __future__ import absolute_import

import re
import time
from PyQt5 import QtCore


class PancakeMachine(object):

    def __init__(self, pinsx, pinsy, motor_delay, pumper_pin, pumper_speed):
        print(pinsx, pinsy)
        self.motor_delay = motor_delay
        self.motor_delay_mutex = QtCore.QMutex()

        self.pumper_speed = pumper_speed
        self.pumper_speed_mutex = QtCore.QMutex()

    def start(self, filename):
        self.stopped = False
        print("pancake start!")

        return self.print_cake()

    def stop(self):
        self.stopped = True

    def changeMotorDelay(self, motor_delay):
        print("change motor_delay to", motor_delay)
        self.motor_delay_mutex.lock()
        self.motor_delay = motor_delay
        self.motor_delay_mutex.unlock()

    def testPumper(self):
        self.stopTest = False
        while self.stopTest == False:
            print("pancake pump testing...")
            self.pumper_speed_mutex.lock()
            pumper_speed = self.pumper_speed
            self.pumper_speed_mutex.unlock()

            print("current speed:", pumper_speed)
            time.sleep(1)

    def stopTestPumper(self):
        self.stopTest = True

    def changePumperSpeed(self, speed):
        self.pumper_speed_mutex.lock()
        self.pumper_speed = speed
        self.pumper_speed_mutex.unlock()

    def print_cake(self):
        cnt = 5
        while cnt > 0:
            if self.stopped:
                return False
            print("pancake printing...")
            self.motor_delay_mutex.lock()
            cur_motor_delay = self.motor_delay
            self.motor_delay_mutex.unlock()

            print("current motor_delay:", cur_motor_delay)
            time.sleep(1)
            cnt -= 1
        return True