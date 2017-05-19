import time
import RPi.GPIO as GPIO

out = {
  'ENA': 11,
  'IN1': 13,
  'IN2': 15,
  'IN3': 12,
  'IN4': 16,
  'ENB': 18
}

Direction = 1
Steps = 0
steps_left = 4095

def reset():
  Direction = 1
  Steps = 0
  steps_left = 4095

def set_direction():
  if Direction == 1:
    Steps += 1
  if Direction == 0:
    Steps -= 1
  if Steps > 7:
    Steps = 0
  if Steps < 0: 
    Steps = 7

def step():
  if Steps == 0:
    GPIO.output(out['IN1'], GPIO.LOW) 
    GPIO.output(out['IN2'], GPIO.LOW)
    GPIO.output(out['IN3'], GPIO.LOW)
    GPIO.output(out['IN4'], GPIO.HIGH)
  elif Steps == 1:
    GPIO.output(out['IN1'], GPIO.LOW) 
    GPIO.output(out['IN2'], GPIO.LOW)
    GPIO.output(out['IN3'], GPIO.HIGH)
    GPIO.output(out['IN4'], GPIO.HIGH)
  elif Steps == 2:
    GPIO.output(out['IN1'], GPIO.LOW) 
    GPIO.output(out['IN2'], GPIO.LOW)
    GPIO.output(out['IN3'], GPIO.HIGH)
    GPIO.output(out['IN4'], GPIO.LOW)
  elif Steps == 3:
    GPIO.output(out['IN1'], GPIO.LOW) 
    GPIO.output(out['IN2'], GPIO.HIGH)
    GPIO.output(out['IN3'], GPIO.HIGH)
    GPIO.output(out['IN4'], GPIO.LOW)
  elif Steps == 4:
    GPIO.output(out['IN1'], GPIO.LOW) 
    GPIO.output(out['IN2'], GPIO.HIGH)
    GPIO.output(out['IN3'], GPIO.LOW)
    GPIO.output(out['IN4'], GPIO.LOW)
  elif Steps == 5:
    GPIO.output(out['IN1'], GPIO.HIGH) 
    GPIO.output(out['IN2'], GPIO.HIGH)
    GPIO.output(out['IN3'], GPIO.LOW)
    GPIO.output(out['IN4'], GPIO.LOW)
  elif Steps == 6:
    GPIO.output(out['IN1'], GPIO.HIGH) 
    GPIO.output(out['IN2'], GPIO.LOW)
    GPIO.output(out['IN3'], GPIO.LOW)
    GPIO.output(out['IN4'], GPIO.LOW)
  elif Steps == 7:
    GPIO.output(out['IN1'], GPIO.HIGH) 
    GPIO.output(out['IN2'], GPIO.LOW)
    GPIO.output(out['IN3'], GPIO.LOW)
    GPIO.output(out['IN4'], GPIO.HIGH)
  else:
    GPIO.output(out['IN1'], GPIO.LOW) 
    GPIO.output(out['IN2'], GPIO.LOW)
    GPIO.output(out['IN3'], GPIO.LOW)
    GPIO.output(out['IN4'], GPIO.LOW)
  set_direction()

def loop():
  print(steps_left)
  while steps_left > 0:
    step()
    time.sleep(0.1)
    steps_left -= 1

