import os
import re

REGEX_STR = r'^(?P<depth>\d+).{2}(?P<range>\d+)$'

def parse_input():
    FILENAME = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(FILENAME) as f:
        p = re.compile(REGEX_STR)
        output = []
        for line in f:
            match = p.match(line)
            output.append(match.groupdict())
        return output

class Firewall(object):
    '''The task firewall class'''
    def __init__(self, length):
        self.segments = [0] * length
        self.calc_depth(parse_input())
        self.segments = tuple(self.segments)
        self.picosecond = 0

    def __repr__(self):
        return self.segments

    def calc_depth(self, depthinput):
        '''takes in processed dict to calculate depth'''
        for item in depthinput:
            index = int(item['depth'])
            frange = int(item['range'])
            self.segments[index] = frange

    def advance_second(self):
        self.picosecond += 1

    def set_second(self, i):
        self.picosecond = i

    def reset_second(self):
        self.picosecond = 0

    def check_severity(self, index):
        if self.picosecond == 0 and index == 0:
            return index * self.segments[index]
        else:
            at_zero_when = (self.segments[index] - 1) * 2
            if self.picosecond % at_zero_when == 0:
                return index * self.segments[index]
            else:
                return 0

    def check_nocoll(self):
        self.reset_second()
        while True:
            for index, item in enumerate(self.segments):
                if item != 0 and (self.picosecond + index) % ((item - 1) * 2) == 0:
                    break
            else:
                return self.picosecond
            self.advance_second()

firewall = Firewall(99)

def check_severity(startsec):
    result = []
    firewall.set_second(startsec)
    for i in range(99):
        sev = firewall.check_severity(i)
        firewall.advance_second()
        result.append(sev)
    return sum(result)

print(check_severity(0))
print(firewall.check_nocoll())
