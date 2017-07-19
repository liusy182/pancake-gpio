from __future__ import absolute_import

# from threading import Thread, Event
import RPi.GPIO as GPIO
import time


class StepperMotor(object):
    def __init__(self, pins):
        self.pins = pins
        self.pos = 0
        self.steps = 40

    def move_one_cycle(self, dir, delay):
        if dir == 1:
            self.forward(0.0005)
        else:
            self.backward(0.0005)

    def forward(self, delay):
        """
        :param delay: the delay in each step
        :param steps: how many steps should this iteration run
        :return: nothing
        """
        GPIO.output(self.pins['DIR'], 1)
        for i in range(self.steps):
            GPIO.output(self.pins['IN'], 1)
            time.sleep(delay)
            GPIO.output(self.pins['IN'], 0)

    def backward(self, delay):
        """
        :param delay: the delay in each step
        :param steps: how many steps should this iteration run
        :return: nothing
        """
        GPIO.output(self.pins['DIR'], 0)
        for i in range(self.steps):
            GPIO.output(self.pins['IN'], 1)
            time.sleep(delay)
            GPIO.output(self.pins['IN'], 0)

    def forwardX_200(self):
        GPIO.output(self.pins['DIR'], 0)
        GPIO.output(self.pins['IN'], 1)
