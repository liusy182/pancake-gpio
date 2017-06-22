from __future__ import absolute_import

import time

# from threading import Thread, Event
import RPi.GPIO as GPIO


class StepperMotor(object):

    def __init__(self, pins):
        self.pins = pins
        self.delay = 0.001
        self.pos = 0

    def move_one_cycle(self, dir=1):
        if dir == 1:
            self.forward(self.delay, 8)
        else:
            self.backward(self.delay, 8)

    def forward(self, delay, steps):
        """
        :param delay: the delay in each step
        :param steps: how many steps should this iteration run
        :return: nothing
        """
        for i in range(0, steps):
            self.set_step(0, 0, 0, 1)
            time.sleep(delay)
            self.set_step(0, 0, 1, 1)
            time.sleep(delay)
            self.set_step(0, 0, 1, 0)
            time.sleep(delay)
            self.set_step(0, 1, 1, 0)
            time.sleep(delay)
            self.set_step(0, 1, 0, 0)
            time.sleep(delay)
            self.set_step(1, 1, 0, 0)
            time.sleep(delay)
            self.set_step(1, 0, 0, 0)
            time.sleep(delay)
            self.set_step(1, 0, 0, 1)
            time.sleep(delay)

    def backward(self, delay, steps):
        """
        :param delay: the delay in each step
        :param steps: how many steps should this iteration run
        :return: nothing
        """
        for i in range(0, steps):
            self.set_step(1, 0, 0, 1)
            time.sleep(delay)
            self.set_step(1, 0, 0, 0)
            time.sleep(delay)
            self.set_step(1, 1, 0, 0)
            time.sleep(delay)
            self.set_step(0, 1, 0, 0)
            time.sleep(delay)
            self.set_step(0, 1, 1, 0)
            time.sleep(delay)
            self.set_step(0, 0, 1, 0)
            time.sleep(delay)
            self.set_step(0, 0, 1, 1)
            time.sleep(delay)
            self.set_step(0, 0, 0, 1)
            time.sleep(delay)

    def set_step(self, w1, w2, w3, w4):
        GPIO.output(self.pins["IN1"], w1)
        GPIO.output(self.pins["IN2"], w2)
        GPIO.output(self.pins["IN3"], w3)
        GPIO.output(self.pins["IN4"], w4)
