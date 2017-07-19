from __future__ import absolute_import

import time

# from threading import Thread, Event
import RPi.GPIO as GPIO


class Pumper(object):
    def __init__(self, pin1, pin2, cycle_time):
        self.pin1 = pin1
        self.pin2 = pin2
        self.cycle_time = cycle_time

    def run_one_cycle(self, on_time):
        GPIO.output(self.pin1, GPIO.HIGH)
        time.sleep(on_time)
        #GPIO.output(self.pin1, GPIO.LOW)
        time.sleep(self.cycle_time - on_time)

    def reset(self):
        GPIO.output(self.pin1, GPIO.LOW)
        #GPIO.output(self.pin2, GPIO.LOW)