import RPi.GPIO as GPIO
import time

stepper_motor_out = {
  'ENA': 11,
  'IN1': 13,
  'IN2': 15,
  'IN3': 12,
  'IN4': 16,
  'ENB': 18
}

stepper_motor_in = {
  21: 'IN1',
  22: 'IN2',
  23: 'IN3',
  24: 'IN4'
}

def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(stepper_motor_in.keys(), GPIO.IN)
  GPIO.setup(stepper_motor_out.values(), GPIO.OUT, initial=GPIO.HIGH)

def run_loop():
    while True:
      for key, val in stepper_motor_in:
        if GPIO.input(key):
          GPIO.output(stepper_motor_out[val], GPIO.HIGH)
        else:
          GPIO.output(stepper_motor_out[val], GPIO.LOW)
      time.sleep(0.1)


if __name__ == "__main__":
  setup()
  run_loop()