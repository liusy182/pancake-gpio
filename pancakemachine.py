from __future__ import absolute_import

import re
import time
from PyQt5 import QtCore

import RPi.GPIO as GPIO

from pancake.steppermotor import StepperMotor


class PancakeMachine(object):

    def __init__(self, pinsx, pinsy, delay):
        self.motorX = StepperMotor(pinsx)
        self.motorY = StepperMotor(pinsy)
        self.delay = delay
        self.delay_mutex = QtCore.QMutex()

    def start(self, filename):
        self.stopped = False
        instructions = self.parse(filename)
        return self.print_cake(instructions)

    def stop(self):
        self.stopped = True

    def changeDelay(self, delay):
        self.delay_mutex.lock()
        self.delay = delay
        self.delay_mutex.unlock()

    def parse(self, filename):
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


    def print_cake(self, cmds):
        print("Pancake printing...")
        for cmd in cmds:
            if self.stopped:
                print("Pancake stopping...")
                return False
            
            if cmd.startswith('G00'):
                m = re.search('G00\sX(\S+)\sY(\S+)', cmd)
                if not m:
                    continue
                x = m.group(1)
                y = m.group(2)
                self.move_line(int(float(x)), int(float(y)))
            elif cmd.startswith('G28'):
                # Resets X, Y
                # self.move_line(0, 0)
                continue
            elif cmd.startswith('G4'):
                # Pause for certain milli secs
                m = re.search('G00\sP(\S+)', cmd)
                if not m:
                    continue
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
        return True


    def move_line(self, newx, newy):
        """
        Function to move two motors in line
        :param newx: 
        :param newy: 
        :return: 
        """
        dx = newx - self.motorX.pos
        dy = newy - self.motorY.pos
        dirX = 1 if dx > 0 else -1
        dirY = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)

        self.delay_mutex.lock()
        cur_delay = self.delay
        self.delay_mutex.unlock()

        if dx > dy:
            print("Motor X Moving ", dirX)
            over = dx/2
            for i in range(0, dx):
                # Todo: conversion between int to steps
                self.motorX.move_one_cycle(dirX, cur_delay)
                over += dy
                if over >= dx:
                    over -= dx
                    self.motorY.move_one_cycle(dirY, cur_delay)
        else:
            print("Motor Y Moving ", dirY)
            over = dy/2
            for i in range(0, dy):
                self.motorX.move_one_cycle(dirX, cur_delay)
                over += dx
                if over >= dy:
                    over -= dy
                    self.motorY.move_one_cycle(dirY, cur_delay)
        
        self.motorX.pos = newx
        self.motorY.pos = newy


