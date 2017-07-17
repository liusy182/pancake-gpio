from __future__ import absolute_import

import re
import time
from PyQt5 import QtCore


class PancakeMachine(object):

    def __init__(self, pinsx, pinsy, delay):
        print(pinsx, pinsy)
        self.delay = delay
        self.delay_mutex = QtCore.QMutex()

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