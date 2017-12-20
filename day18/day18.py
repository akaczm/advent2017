import os

instructions_demo = '''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''

FILENAME = os.path.join(os.path.dirname(__file__), 'input.txt')
def get_input():
    with open(FILENAME) as f:
        return f.read()

class Program(object):
    def __init__(self, pid):
        self.pid = pid
        self.registers = dict.fromkeys(map(chr, range(97, 113)), 0)
        self.registers['p'] = self.pid
        self.sound = 0
        self.i = 0
        self.sent = 0
        self.queue = []
        self.link = None

    def add_queue(self, num):
        self.queue.append(num)

    def exec_instructions(self, instr_l):
        
        instr_s = instr_l.split('\n')
        while self.i >= 0 and self.i < len(instr_s):
            instr = instr_s[self.i][:3]
            vals = instr_s[self.i][3:]
            res = self.instructions(instr, vals)
            if res != None:
                self.i += res
            else:
                self.i += 1

    def exec_singular(self, instr_l):
        instr_s = instr_l.split('\n')
        instr = instr_s[self.i][:3]
        vals = instr_s[self.i][3:]
        res = self.instructions(instr, vals)
        if res == "EOF":
            self.link.exec_singular(instr_l)
            return True
        elif res != None:
            self.i += res
            return True
        else:
            self.i += 1
            return True

    def exec_parallel(self, instr_l):
        val1 = self.exec_singular(instr_l)
        val2 = self.link.exec_singular(instr_l)

        if not val1 or not val2:
            return False
        else:
            return True

    def set_link(self, program):
        self.link = program

    def to_buffer(self, val):
        self.queue.append(val)

    def send_val(self, val):
        self.link.to_buffer(val)

    def instructions(self, instr, vals):
        vals = vals.strip()
        #if instr == 'snd': #part1 solution
        #    try:
        #        self.sound = int(vals)
        #    except ValueError:
        #        self.sound = self.registers[vals]
        if instr == 'snd':
            try:
                buffer = int(vals)
            except ValueError:
                buffer = self.registers[vals]
            self.sent += 1
            self.send_val(buffer)
        if instr == 'set':
            vals = vals.split()
            vals = list(map(str.strip, vals))
            try:
                self.registers[vals[0]] = int(vals[1])
            except ValueError:
                self.registers[vals[0]] = self.registers[vals[1]]
        if instr == 'add':
            vals = vals.split()
            vals = list(map(str.strip, vals))
            try:
                self.registers[vals[0]] += int(vals[1])
            except ValueError:
                self.registers[vals[0]] += self.registers[vals[1]]
        if instr == 'mul':
            vals = vals.split()
            vals = list(map(str.strip, vals))
            try:
                self.registers[vals[0]] *= int(vals[1])
            except ValueError:
                self.registers[vals[0]] *= self.registers[vals[1]]
        if instr == 'mod':
            vals = vals.split()
            vals = list(map(str.strip, vals))
            try:
                self.registers[vals[0]] %= int(vals[1])
            except ValueError:
                self.registers[vals[0]] %= self.registers[vals[1]]
        if instr == 'rcv':
        #    try:
        #        if int(vals) != 0:
        #            self.registers[vals] = self.sound
        #    except ValueError:
        #        if self.registers[vals] != 0:
        #            self.registers[vals] = self.sound
            try:
                self.registers[vals] = self.queue.pop(0)
            except IndexError:
                return "EOF"
        if instr == 'jgz':
            vals = vals.split()
            vals = list(map(str.strip, vals))
            try:
                if self.registers[vals[0]] > 0:
                    try:
                        return int(vals[1])
                    except ValueError:
                        return int(self.registers[vals[1]])
            except KeyError:
                if int(vals[0]) > 0:
                    try:
                        return int(vals[1])
                    except ValueError:
                        return int(self.registers[vals[1]])

program1 = Program(0)
program2 = Program(1)
program1.set_link(program2)
program2.set_link(program1)
try:
    while program1.exec_parallel(get_input()): 
        pass
except RecursionError:
    print(program1.sent)
    print(program2.sent)