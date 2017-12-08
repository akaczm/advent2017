import re
import operator
from timeit import default_timer as timer

REGEX_STR = r'^(?P<reg1>\w+)\s(?P<instr>\w+)\s(?P<int>-?\d+)\s(if\s(?P<reg2>\w+)\s(?P<cond>\S+)\s(?P<num>-?\d+))$'

def parse_input():
    with open('input.txt') as inp:
        outputlist = []
        p = re.compile(REGEX_STR)
        for line in inp:
            match = p.match(line)
            outputlist.append(match.groupdict())
        return outputlist

def get_register(reglist, reg):
    try:
        return reglist[reg]
    except KeyError:
        return 0

def calc_cond(instruction, reg1, reg2):
    instr = instruction['cond']
    num = instruction['num']
    reg1 = int(reg1)
    reg2 = int(reg2)
    num = int(num)
    if instr == '>':
        if reg2 > num:
            return True
        else: return False
    elif instr == '<':
        if reg2 < num:
            return True
        else: return False
    elif instr == '>=':
        if reg2 >= num:
            return True
        else: return False
    elif instr == '<=':
        if reg2 <= num:
            return True
        else: return False
    elif instr == '==':
        if reg2 == num:
            return True
        else: return False
    elif instr == '!=':
        if reg2 != num:
            return True
        else: return False

def calc_list(reg1, instr, num):
    reg1 = int(reg1)
    num = int(num)
    if instr == 'inc':
        return(reg1 + num)
    elif instr == 'dec':
        return(reg1 - num)


def calc_instruction(reglist, instruction, maxresult):
    reg1 = get_register(reglist, instruction['reg1'])
    reg2 = get_register(reglist, instruction['reg2'])
    
    if calc_cond(instruction, reg1, reg2):
        result = calc_list(reg1, instruction['instr'], instruction['int'])
        if result > maxresult['max']:
            maxresult['max'] = result
        reglist[instruction['reg1']] = result

def main():
    start = timer()
    instructions = parse_input()
    reglist = dict()
    maxresult = {'max': 0}
    for instruction in instructions:
        calc_instruction(reglist, instruction, maxresult)
    end = timer()
    print(max(reglist, key=reglist.get), max(reglist.values()), maxresult['max'])
    print("Time taken: %f" % (end - start))

main()