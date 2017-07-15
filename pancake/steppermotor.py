from __future__ import absolute_import

import time

# from threading import Thread, Event
import RPi.GPIO as GPIO


class StepperMotor(object):
    def __init__(self, pins):
        self.pins = pins
        self.pos = 0

    def move_one_cycle(self, dir, delay):
        if dir == 1:
            self.forward(delay, 20)
        else:
            self.backward(delay, 20)

    def forward(self, delay, steps):
        """
        :param delay: the delay in each step
        :param steps: how many steps should this iteration run
        :return: nothing
        """
        GPIO.output(self.pins['DIR'], 1)
        for i in range(0, steps):
            GPIO.output(self.pins['IN'], 1)
        GPIO.output(self.pins['IN'], 0)

    def backward(self, delay, steps):
        """
        :param delay: the delay in each step
        :param steps: how many steps should this iteration run
        :return: nothing
        """
        GPIO.output(self.pins['DIR'], 0)
        for i in range(0, steps):
            GPIO.output(self.pins['IN'], 1)
        GPIO.output(self.pins['IN'], 0)
