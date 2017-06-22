from __future__ import absolute_import

import re

class Ops(object):
    MOVE = 1
    MOTOR = 2


class GCodeParser(object):
    def __init__(self):
        self.idx = -1
        self.ops = []
        self.px = 0
        self.py = 0
        self.step_delay = 0.001

    def parse(self, filename):
        """
        Possible Commands 
            G00 :
            G28 : Home all Axis
            G4  : Pause
            M84 : Motors off
            M106: Pump on 
            M107: Pump off
            
        :param filename: the gcode input file 
        :return: 
        """
        lines = []
        with open(filename, 'r') as f:
            lines = f.readlines()

        for l in lines:
            if l.startswith('G00'):
                self._parse_move(l)
            elif l.startswith('M'):
                self._parse_motor(l)

    def parse_move(self, l):
        m = re.search('G00\sX(\S+)\sY(\S+)', l)
        if not m:
            return
        x = m.group(1)
        y = m.group(2)
        self._move_line(x, y)
        self.idx += 1
        # self.ops.append({'ops': Ops.MOVE, 'x': x, 'y', y})

    def _move_line(self, newx, newy):
        """
        
        :param self: 
        :param newx: 
        :param newy: 
        :return: 
        """
        dx = newx - self.px
        dy = newy - self.py
        dirx = 1 if dx > 0 else -1
        diry = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)
        if dx > dy:
            over = dx / 2
            for i in range(0, dx):
                # Todo: conversion between int to steps
                clockwise(0.005, 8) if dirx == 1 else anti
                over += dy
                if over >= dx:
                    over -= dx
                    motorYStep(diry)
                pause(self.step_delay)  # pause for delay
        else:
            over = dy / 2
            for i in range(0, dy):
                motorYStep(diry)
                over += dx
                if over >= dy:
                    over -= dy
                    motorXStep(dirx)
                pause(self.step_delay)
        self.px = newx
        self.py = newy

    def _parse_motor(self, l):
        pass

    def get_next_ops(self):
        pass
