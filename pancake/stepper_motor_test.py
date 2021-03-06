import RPi.GPIO as GPIO

from steppermotor import StepperMotor

# In case other pins required. temporary put pin_x and pin_y as list
PINS_X = {
    'IN': 11,
    'DIR': 19
}

PINS_Y = {
    'IN': 12,
    'DIR': 16
}

motorX = StepperMotor(PINS_X)
motorY = StepperMotor(PINS_Y)


def setup():
    """
    Setup function to initialize GPIO Board
    :return:
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(list(PINS_X.values()), GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(list(PINS_Y.values()), GPIO.OUT, initial=GPIO.HIGH)


if __name__ == "__main__":
    setup()
    # print("x forwaring 200")
    for i in range(200):
        motorX.forward(0.005)
    for i in range (200):
        motorY.backward(0.005)

    GPIO.cleanup()

