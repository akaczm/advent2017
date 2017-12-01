'''The captcha requires you to review a sequence of digits
(your puzzle input) and find the sum of all digits that match
the next digit in the list. The list is circular, so the digit
after the last digit is the first digit in the list.'''

from itertools import cycle, tee, islice, chain

def next_item(iterable):
    citerable = cycle(iterable)
    currents, nexts, mids = tee(citerable, 3)
    nexts = islice(nexts, 1, None)
    mid = int(len(iterable)/2)
    mids = islice(mids, mid, None)
    return zip(currents, nexts, mids)

def solve_captcha(puzzle_input, matchtype="nexts"):
    puzzle_digits = str(puzzle_input)
    
    equal_match = []
    i = 0
    for current, nxt, mid in next_item(puzzle_digits):
        i += 1
        if matchtype == "nexts":
            if current == nxt:
                equal_match.append(int(current))
        if matchtype == "mids":
            if current == mid:
                equal_match.append(int(current))
        if len(puzzle_digits) <= i:
            break
    if equal_match == []:
        return 0
    else:
        return(sum(equal_match))
