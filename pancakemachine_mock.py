from __future__ import absolute_import

import re
import time
from PyQt5 import QtCore


class PancakeMachine(object):

    def __init__(self, pinsx, pinsy, delay, pumper_pin, pumper_speed):
        print(pinsx, pinsy)
        self.delay = delay
        self.delay_mutex = QtCore.QMutex()

        self.pumper_speed = pumper_speed
        self.speed_mutex = QtCore.QMutex()

    def start(self, filename):
        self.stopped = False
        print("pancake start!")

        return self.print_cake()

    def stop(self):
        self.stopped = True

    def changeDelay(self, delay):
        print("change delay to", delay)
        self.delay_mutex.lock()
        self.delay = delay
        self.delay_mutex.unlock()

    def testPumper(self):
        self.stopTest = False
        while self.stopTest == False:
            print("pancake pump testing...")
            self.speed_mutex.lock()
            pumper_speed = self.pumper_speed
            self.speed_mutex.unlock()

            print("current speed:", pumper_speed)
            time.sleep(1)

    def stopTestPumper(self):
        self.stopTest = True

    def changePumperSpeed(self, speed):
        self.speed_mutex.lock()
        self.pumper_speed = speed
        self.speed_mutex.unlock()

    def print_cake(self):
        cnt = 5
        while cnt > 0:
            if self.stopped:
                return False
            print("pancake printing...")
            self.delay_mutex.lock()
            cur_delay = self.delay
            self.delay_mutex.unlock()

            print("current delay:", cur_delay)
            time.sleep(1)
            cnt -= 1
        return True