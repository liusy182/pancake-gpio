from __future__ import absolute_import

import re
import time
import threading


class PancakeMachine(object):

    def __init__(self, pinsx, pinsy, delay):
        print(pinsx, pinsy)
        self.delay = delay
        self.delay_lock = threading.Lock()

    def start(self, filename):
        self.stopped = False
        print("pancake start!")

        self.print_thread = threading.Thread(target=self.print_cake)
        self.print_thread.start()

    def stop(self):
        self.stopped = True

    def changeDelay(self, delay):
        self.delay_lock.acquire()
        self.delay = delay
        self.delay_lock.release()

    def print_cake(self):
        while self.stopped == False:
            print("pancake printing...")
            self.delay_lock.acquire()
            cur_delay = self.delay
            self.delay_lock.release()

            print("current delay:", cur_delay)
            time.sleep(1)