import sys
import PyQt5
from PyQt5.QtWidgets import *

import RPi.GPIO as GPIO

from mainwindow import MainWindow

# In case other pins required. temporary put pin_x and pin_y as list
PINS_X = {
    'IN': 11,
    'DIR': 15
}

PINS_Y = {
    'IN': 8,
    'DIR': 16
}

PIN_PUMPER1 = 19
PIN_PUMPER2 = 14

PIN_ENABLE_MOTOR = 10

def setup():
    """
    Setup function to initialize GPIO Board
    :return: 
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(list(PINS_X.values()), GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(list(PINS_Y.values()), GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN_PUMPER1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(PIN_ENABLE_MOTOR, GPIO.OUT, initial=GPIO.HIGH)
    
def cleanup():
    GPIO.cleanup()
      

def main():
    setup()
    app = QApplication(sys.argv)
    form = MainWindow(PINS_X, PINS_Y, PIN_PUMPER1, PIN_PUMPER2, PIN_ENABLE_MOTOR)
    form.show()
    sys.exit(app.exec_())
    cleanup()

if __name__ == "__main__":
    main()

