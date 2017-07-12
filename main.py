import sys
import PyQt5
from PyQt5.QtWidgets import *

from mainwindow import MainWindow

# In case other pins required. temporary put pin_x and pin_y as list
PINS_X = {
    'IN': 11,
    'DIR': 15
}

PINS_Y = {
    'IN': 12,
    'DIR': 16
}

def setup():
    """
    Setup function to initialize GPIO Board
    :return: 
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(PINS_X.values(), GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PINS_Y.values(), GPIO.OUT, initial=GPIO.HIGH)
    
def cleanup():
    GPIO.cleanup()
      

def main():
    #setup()
    app = QApplication(sys.argv)
    form = MainWindow(PINS_X, PINS_Y)
    form.show()
    sys.exit(app.exec_())
    #cleanup()

if __name__ == "__main__":
    main()

