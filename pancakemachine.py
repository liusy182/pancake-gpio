from __future__ import absolute_import

import re
import time
from PyQt5 import QtCore
from decimal import *
from pancake.pumper import Pumper
from pancake.steppermotor import StepperMotor


class PancakeMachine(object):
    def __init__(self, pinsx, pinsy, motor_delay, pumper_pin1, pumper_pin2, pumper_speed, cycle_time, motor_pin_enable):
        self.motor = StepperMotor(pinsx, pinsy, motor_pin_enable)
        self.motor_delay = motor_delay
        self.motor_delay_mutex = QtCore.QMutex()

        self.pumper = Pumper(pumper_pin1, pumper_pin2, cycle_time)
        self.pumper_speed = pumper_speed
        self.pumper_speed_mutex = QtCore.QMutex()

    def start(self, filename):
        self.stopped = False
        instructions = self.parse(filename)
        return self.print_cake(instructions)

    def stop(self):
        self.stopped = True

    def changeMotorDelay(self, motor_delay):
        self.motor_delay_mutex.lock()
        self.motor_delay = motor_delay
        self.motor_delay_mutex.unlock()

    def testPumper(self):
        self.stopTest = False
        while self.stopTest == False:
            print("pancake pump testing...")
            self.pumper_speed_mutex.lock()
            pumper_speed = self.pumper_speed
            self.pumper_speed_mutex.unlock()

            print("current speed:", pumper_speed)
            self.pumper.run_one_cycle(pumper_speed)
        # close it
        self.pumper.reset()

    def stopTestPumper(self):
        self.stopTest = True

    def changePumperSpeed(self, speed):
        self.pumper_speed_mutex.lock()
        self.pumper_speed = speed
        self.pumper_speed_mutex.unlock()

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
        self.motor.enable_motors(1)
        pumper_speed = self.pumper_speed

        for cmd in cmds:
            if self.stopped:
                print("Pancake stopping...")
                self.motor.enable_motors(0)
                return False

            print(cmd)
            if cmd.startswith('G00'):
                m = re.search('G00\sX(\S+)\sY(\S+)', cmd)
                if not m:
                    continue
                x = m.group(1)
                y = m.group(2)
                # Change to round
                self.move_line(round(float(x)), round(float(y)))
            elif cmd.startswith('G28'):
                # Resets X, Y
                # self.move_line(0, 0)
                continue
            elif cmd.startswith('G4'):
                # Pause for certain milli secs
                m = re.search('G4\sP(\S+)', cmd)
                if not m:
                    continue
                print("Sleep time " + str(m.group(1)))
                time.sleep(m.group(1) / 1000)
            elif cmd.startswith('M84'):
                # Motors Off
                continue
            elif cmd.startswith('M106'):
                # Pump on
                self.changePumperSpeed(pumper_speed)
                continue
            elif cmd.startswith('M107'):
                # Pump off
                self.changePumperSpeed(0)
                continue
        self.motor.enable_motors(0)
        self.changePumperSpeed(pumper_speed)
        return True

    def move_line(self, newx, newy):
        """
        Function to move two motors in line
        :param newx: 
        :param newy: 
        :return: 
        """
        dx = newx - self.motor.posx
        dy = newy - self.motor.posy
        dirX = 1 if dx > 0 else -1
        dirY = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)

        self.motor_delay_mutex.lock()
        cur_motor_delay = self.motor_delay
        self.motor_delay_mutex.unlock()

        if dx > dy:
            print("Motor X Moving ", dirX)
            over = dx / 2
            for i in range(0, dx):
                # Todo: conversion between int to steps
                over += dy
                if over >= dx:
                    over -= dx
                    self.motor.move_one_cycle(1, 1, dirX, dirY, cur_motor_delay)
                else:
                    self.motor.move_one_cycle(1, 0, dirX, dirY, cur_motor_delay)

        else:
            print("Motor Y Moving ", dirY)
            over = dy / 2
            for i in range(0, dy):
                over += dx
                if over >= dy:
                    over -= dy
                    self.motor.move_one_cycle(1, 1, dirX, dirY, cur_motor_delay)
                else:
                    self.motor.move_one_cycle(0, 1, dirX, dirY, cur_motor_delay)

        self.motor.posx = newx
        self.motor.posy = newy
