'''The captcha requires you to review a sequence of digits
(your puzzle input) and find the sum of all digits that match
the next digit in the list. The list is circular, so the digit
after the last digit is the first digit in the list.'''

from itertools import cycle, tee, islice, chain

def next_item(iterable):
    currents, nexts = tee(iterable, 2)
    nexts = islice(nexts, 1, None)
    return zip(currents, nexts)

def solve_captcha(puzzle_input):
    puzzle_digits = str(puzzle_input)
    
    equal_match = []
    i = 0
    for current, nxt in next_item(cycle(puzzle_digits)):
        i += 1
        if current == nxt:
            equal_match.append(int(current))
        if len(puzzle_digits) <= i:
            break
    if equal_match == []:
        return 0
    else:
        return(sum(equal_match))
