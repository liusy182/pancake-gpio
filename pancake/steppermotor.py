
from __future__ import absolute_import
import time
from threading import Thread, Event
import RPi.GPIO as GPIO

PINS_X = {
    'ENA': 11,
    'IN1': 13,
    'IN2': 15,
    'IN3': 12,
    'IN4': 16,
    'ENB': 18
}

PINS_Y = {
    'ENA': 19,
    'IN1': 21,
    'IN2': 23,
    'IN3': 22,
    'IN4': 24,
    'ENB': 26
}

class StepperMotor(object):

    # min delay between 2 consecutive steps
    min_interval = 0.005

    def __init__(self, pins, steps):
        self.pins = pins
        self.steps = steps
        self.pos = 0

        self.new_pos = 0
        self.duration = min_interval

        self.e = Event()
        self.e.clear()
        self.t = Thread(target=self._beat)
        self.t.daemon = True
        self.t.start()
        

    def reset(self):
        self.move(0)
        #TODO clean up thread and event

    def get_duration(self, pos):
        return abs(pos - self.pos) * min_interval

    def move(self, pos, duration):
        self.duration = duration if duration else self.get_duration(pos)
        self.new_pos = pos
        self.e.set()

    def _move(self):
        while self.e.wait():
            duration = self.duration
            pos = self.new_pos
            time_slice = duration / abs(pos - self.pos)

            while pos != self.pos and 0 <= self.pos <= self.steps:
                self.pos += 1 * direction
                self._step()
                time.sleep(time_slice)
            self.e.clear()


    def _step(self):
        out = self.pins
        if self.pos % 8 == 0:
            GPIO.output(out['IN1'], GPIO.HIGH) 
            GPIO.output(out['IN2'], GPIO.HIGH)
            GPIO.output(out['IN3'], GPIO.LOW)
            GPIO.output(out['IN4'], GPIO.LOW)
        elif self.pos % 8 == 1:
            GPIO.output(out['IN1'], GPIO.LOW) 
            GPIO.output(out['IN2'], GPIO.HIGH)
            GPIO.output(out['IN3'], GPIO.HIGH)
            GPIO.output(out['IN4'], GPIO.LOW)
        elif self.pos % 8 == 2:
            GPIO.output(out['IN1'], GPIO.LOW) 
            GPIO.output(out['IN2'], GPIO.LOW)
            GPIO.output(out['IN3'], GPIO.HIGH)
            GPIO.output(out['IN4'], GPIO.HIGH)
        elif self.pos % 8 == 3:
            GPIO.output(out['IN1'], GPIO.HIGH) 
            GPIO.output(out['IN2'], GPIO.LOW)
            GPIO.output(out['IN3'], GPIO.LOW)
            GPIO.output(out['IN4'], GPIO.HIGH)
        elif self.pos % 8 == 4:
            GPIO.output(out['IN1'], GPIO.HIGH) 
            GPIO.output(out['IN2'], GPIO.HIGH)
            GPIO.output(out['IN3'], GPIO.LOW)
            GPIO.output(out['IN4'], GPIO.LOW)
        elif self.pos % 8 == 5:
            GPIO.output(out['IN1'], GPIO.LOW) 
            GPIO.output(out['IN2'], GPIO.HIGH)
            GPIO.output(out['IN3'], GPIO.HIGH)
            GPIO.output(out['IN4'], GPIO.LOW)
        elif self.pos % 8 == 6:
            GPIO.output(out['IN1'], GPIO.LOW) 
            GPIO.output(out['IN2'], GPIO.LOW)
            GPIO.output(out['IN3'], GPIO.HIGH)
            GPIO.output(out['IN4'], GPIO.HIGH)
        elif self.pos % 8 == 7:
            GPIO.output(out['IN1'], GPIO.HIGH) 
            GPIO.output(out['IN2'], GPIO.LOW)
            GPIO.output(out['IN3'], GPIO.LOW)
            GPIO.output(out['IN4'], GPIO.HIGH)
        else:
            GPIO.output(out['IN1'], GPIO.LOW) 
            GPIO.output(out['IN2'], GPIO.LOW)
            GPIO.output(out['IN3'], GPIO.LOW)
            GPIO.output(out['IN4'], GPIO.LOW)

class StepperMotorController(object):
    def __init(self):
        GPIO.setup(PINS_X.values(), GPIO.OUT, initial=GPIO.HIGH)
        self.motor_x = StepperMotor(pins=PINS_X, steps=1000)

        GPIO.setup(PINS_Y.values(), GPIO.OUT, initial=GPIO.HIGH)
        self.motor_y = StepperMotor(pins=PINS_Y, steps = 2000)

    def move(self, x, y):
        duration = max(self.motor_x.get_duration(x), self.motor_y.get_duration(y))
        self.motor_x.move(x, duration)
        self.motor_y.move(y, duration)
        #need to buffer a longer delay
        time.sleep(duration * 1.2)