
from __future__ import absolute_import
import re

class Ops(object):
    MOVE = 1
    MOTOR = 2

class GCodeParser(object):
    def __init__(self):
        self.idx = -1
        self.ops = []

    def parse(self, filename):
        lines = []
        with open(filename, 'r') as f:
            lines = f.readlines()

        for l in lines:
            if l.startswith('G00'):
                self._parse_move(l)
            elif l.startswith('M'):
                self._parse_motor(l)

    def _parse_move(self, l):
        m = re.search('G00\sX(\S+)\sY(\S+)', l)
        if not m:
            return
        x = m.group(1)
        y = m.group(2)
        self.idx += 1
        self.ops.append({'ops': Ops.MOVE, 'x': x, 'y', y})
    
    def _parse_motor(self, l):
        pass

    def get_next_ops(self):
        pass


