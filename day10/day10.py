import os
import numpy
from functools import reduce
from operator import xor

def parse_input():
    FILENAME = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(FILENAME) as f:
        content = f.read()
        return content.rstrip('\n').split(',')

def parse_input_ascii():
    FILENAME = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(FILENAME, mode='r', ) as f:
        content = f.read()
        content = content.rstrip('\n')
        content = [ord(c) for c in content]
        content = content + [17, 31, 73, 47, 23]
        return content

def knothash(lengths, current_position=0, skip_size=0, numlist=list(range(256))):
    lengths = list(map(int, lengths))
    for length in lengths:
        if length == 0 or length == 1:
            current_position += (length + skip_size)
            current_position = current_position % len(numlist)
            skip_size += 1
            continue
        start_index = current_position
        end_index = (current_position + length) % len(numlist)
        if start_index > end_index:
            part1 = numlist[start_index:]
            part2 = numlist[:end_index]
            revlist = part1 + part2
            revlist = list(reversed(revlist))
            numlist[start_index:] = revlist[:len(part1)]
            numlist[:end_index] = revlist[len(part1):]
        else:
            numlist[start_index:end_index] = list(reversed(numlist[start_index:end_index]))
        current_position += (length + skip_size)
        current_position = current_position % len(numlist)
        skip_size += 1
    return(numlist, current_position, skip_size)

def knothash_rounds(rounds):
    lengths = parse_input_ascii()
    values = dict()
    values['current_position'] = 0
    values['skip_size'] = 0
    values['numlist'] = list(range(256))
    while rounds > 0:        
        values['numlist'], values['current_position'], values['skip_size'] = knothash(lengths, values['current_position'], values['skip_size'], values['numlist'])        
        rounds -= 1
    return values['numlist']

def dense_hash(l, n=16):
    chunks = [l[i:i + n] for i in range(0, len(l), n)]
    dense = []
    dense_str = ''
    for chunk in chunks:
        dense.append((reduce(xor, chunk)))
    for item in dense:
        dense_str = dense_str + "%0.2X" % item
    return dense_str
    

hashlist = knothash(parse_input())[0]
print(hashlist[0] * hashlist[1])
print(dense_hash(knothash_rounds(64)))