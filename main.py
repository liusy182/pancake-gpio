import RPi.GPIO as GPIO
import stepper


def setup():
    GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(stepper.stepper_motor_in.keys(), GPIO.IN)
    GPIO.setup(stepper.out.values(), GPIO.OUT, initial=GPIO.HIGH)


def run_loop():
    while True:
        stepper.anticlockwise(0.005, 600)
        stepper.clockwise(0.005, 600)


if __name__ == "__main__":
    setup()
    run_loop()
