from __future__ import absolute_import

# from threading import Thread, Event
import RPi.GPIO as GPIO
import time


class StepperMotor(object):
    def __init__(self, pinsx, pinsy, pin_enable):
        self.posx = 0
        self.posy = 0
        self.pinsx = pinsx
        self.pinsy = pinsy
        self.steps = 6
        self.pin_enable = pin_enable

    def move_one_cycle(self, enx, eny, dirx, diry, delay=0.002):
        GPIO.output(self.pinsx['DIR'], 1 if dirx == 1 else 0)
        GPIO.output(self.pinsy['DIR'], 1 if diry == 1 else 0)

        for i in range(self.steps):
            GPIO.output(self.pinsx['IN'], 1 if enx == 1 else 0)
            GPIO.output(self.pinsy['IN'], 1 if eny == 1 else 0)
            time.sleep(delay)
            GPIO.output(self.pinsx['IN'], 0)
            GPIO.output(self.pinsy['IN'], 0)
            time.sleep(delay)


            # def forward(self, delay):
            #     """
            #     :param delay: the delay in each step
            #     :param steps: how many steps should this iteration run
            #     :return: nothing
            #     """
            #     GPIO.output(self.pins['DIR'], 1)
            #     for i in range(self.steps):
            #         GPIO.output(self.pins['IN'], 1)
            #         time.sleep(delay)
            #         GPIO.output(self.pins['IN'], 0)
            #
            # def backward(self, delay):
            #     """
            #     :param delay: the delay in each step
            #     :param steps: how many steps should this iteration run
            #     :return: nothing
            #     """
            #     GPIO.output(self.pins['DIR'], 0)
            #     for i in range(self.steps):
            #         GPIO.output(self.pins['IN'], 1)
            #         time.sleep(delay)
            #         GPIO.output(self.pins['IN'], 0)

    def enable_motors(self, enable):
        print(self.pin_enable, enable)
        GPIO.output(self.pin_enable, GPIO.LOW if enable == 1 else GPIO.HIGH)
