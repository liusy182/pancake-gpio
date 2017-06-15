import re
import time

import RPi.GPIO as GPIO

from pancake.steppermotor import StepperMotor

PINS_X = {
    'ENA': 11,
    'IN1': 13,
    'IN2': 15,
    'IN3': 12,
    'IN4': 16,
    'ENB': 18
}

PINS_Y = {
    'ENA': 19,
    'IN1': 21,
    'IN2': 23,
    'IN3': 22,
    'IN4': 24,
    'ENB': 26
}

motorX = StepperMotor(PINS_X)
motorY = StepperMotor(PINS_Y)


def setup():
    """
    Setup function to initialize GPIO Board
    :return: 
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PINS_X.values(), GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PINS_Y.values(), GPIO.OUT, initial=GPIO.HIGH)


def parse(filename) -> []:
    """
    function to parse gcode file and converts it to a list of commands
    Possible Commands 
        G00 :
        G28 : Home all Axis
        G4  : Pause
        M84 : Motors off
        M106: Pump on 
        M107: Pump off

    :param filename: the gcode input file 
    :return (list): commands to print the cake
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def print_cake(cmds):
    for cmd in cmds:
        if cmd.startswith('G00'):
            m = re.search('G00\sX(\S+)\sY(\S+)', cmd)
            if not m:
                return
            x = m.group(1)
            y = m.group(2)
            move_line(x, y)
        elif cmd.startswith('G28'):
            # Resets X, Y
            move_line(0, 0)
        elif cmd.startswith('G4'):
            # Pause for certain milli secs
            m = re.search('G00\sP(\S+)', cmd)
            if not m:
                return
            time.sleep(m.group(1) / 1000)
        elif cmd.startswith('M84'):
            # Motors Off
            continue
        elif cmd.startswith('M106'):
            # Pump on
            continue
        elif cmd.startswith('M107'):
            # Pump off
            continue


def move_line(newx, newy):
    """
    Function to move two motors in line
    :param newx: 
    :param newy: 
    :return: 
    """
    dx = newx - motorX.pos
    dy = newy - motorY.pos
    dirX = 1 if dx > 0 else -1
    dirY = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        over = dx / 2
        for i in range(0, dx):
            # Todo: conversion between int to steps
            motorX.move_one_cycle(dirX)
            over += dy
            if over >= dx:
                over -= dx
                motorY.move_one_cycle(dirY)
            time.sleep(0.005)  # pause for delay
    else:
        over = dy / 2
        for i in range(0, dy):
            motorX.move_one_cycle(dirX)
            over += dx
            if over >= dy:
                over -= dy
                motorY.move_one_cycle(dirY)
            time.sleep(0.005)  # pause for delay
    motorX.pos = newx
    motorY.pos = newy


if __name__ == "__main__":
    setup()
    file = "sample.gcode"  # Change to get from Autodesk Cloud Storage later
    instructions = parse(file)
    print_cake(instructions)
