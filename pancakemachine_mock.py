from __future__ import absolute_import

import re
import time


class PancakeMachine(object):

    def __init__(self, pinsx, pinsy):
        print(pinsx, pinsy)

    def start(self, filename):
        self.stopped = False
        print("pancake start!")
        while self.stopped == False:
            print("pancake printing...")
            time.sleep(1)

    def stop(self):
        self.stopped = True
