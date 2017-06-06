import RPi.GPIO as GPIO
import time
import stepper

def setup():
  GPIO.setmode(GPIO.BOARD)
  # GPIO.setup(stepper.stepper_motor_in.keys(), GPIO.IN)
  GPIO.setup(stepper.out.values(), GPIO.OUT, initial=GPIO.HIGH)

def run_loop():
    while True:
      stepper.reset()
      stepper.loop()


if __name__ == "__main__":
  setup()
  run_loop()
