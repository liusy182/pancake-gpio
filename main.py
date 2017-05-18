import RPi.GPIO as GPIO
import time

def setup():
  GPIO.setmode(GPIO.BOARD)

  # Define the GPIO input ports for IR sensors
  input_chan_list = [8, 10, 12]
  GPIO.setup(input_chan_list, GPIO.IN)

  # Define the GPIO output ports for controllering LEDS
  output_chan_list = [22, 24, 26]
  GPIO.setup(output_chan_list, GPIO.OUT, initial=GPIO.HIGH)


def run_loop():
    while True:
      time.sleep(1)

if __name__ == "__main__":
  setup()
  run_loop()