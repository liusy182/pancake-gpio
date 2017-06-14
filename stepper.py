import RPi.GPIO as GPIO
import time

enable_pin_A = 11
enable_pin_B = 18
coil_A_1_pin = 13
coil_A_2_pin = 15
coil_A_3_pin = 12
coil_A_4_pin = 16

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_A_3_pin, GPIO.OUT)
GPIO.setup(coil_A_4_pin, GPIO.OUT)


def clockwise(delay, steps):
    """

    :param delay: the delay in each step
    :param steps: how many steps should this iteration run
    :return: nothing
    """
    for i in range(0, steps):
        set_step(1, 0, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 0, 1)
        time.sleep(delay)
        set_step(1, 0, 0, 1)
        time.sleep(delay)


def anticlockwise(delay, steps):
    """

    :param delay: the delay in each step
    :param steps: how many steps should this iteration run
    :return: nothing
    """
    for i in range(0, steps):
        set_step(1, 0, 0, 1)
        time.sleep(delay)
        set_step(0, 1, 0, 1)
        time.sleep(delay)
        set_step(0, 1, 1, 0)
        time.sleep(delay)
        set_step(1, 0, 1, 0)
        time.sleep(delay)


def set_step(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_A_3_pin, w3)
    GPIO.output(coil_A_4_pin, w4)

