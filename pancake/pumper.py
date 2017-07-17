from __future__ import absolute_import

import time

# from threading import Thread, Event
import RPi.GPIO as GPIO


class Pumper(object):
    def __init__(self, pin, cycle_time):
        self.pin = pin
        self.cycle_time = cycle_time

    def run_one_cycle(self, on_time):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(self.cycle_time - on_time)