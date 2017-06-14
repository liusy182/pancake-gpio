import RPi.GPIO as GPIO
import time

out = {
    'ENA': 11,
    'IN1': 13,
    'IN2': 15,
    'IN3': 12,
    'IN4': 16,
    'ENB': 18
}


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
    GPIO.output(out["IN1"], w1)
    GPIO.output(out["IN2"], w2)
    GPIO.output(out["IN3"], w3)
    GPIO.output(out["IN4"], w4)
