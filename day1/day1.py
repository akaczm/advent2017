'''Advent of Code 2017 Day 1'''

from itertools import cycle, tee, islice, chain

def next_item(iterable):
    '''Create an iterable that is circular
    and contains tuples of three items
    corresponding to the current item,
    next item, and an item halfway away'''
    citerable = cycle(iterable)
    currents, nexts, mids = tee(citerable, 3)
    nexts = islice(nexts, 1, None)
    mid = int(len(iterable)/2)
    mids = islice(mids, mid, None)
    return zip(currents, nexts, mids)

def solve_captcha(puzzle_input, matchtype="nexts"):
    '''Solve the advent captcha, supply matchtime
    of either "nexts" or "mids" according to
    part of the puzzle to solve'''

    #turn integer into a string for iteration
    puzzle_digits = str(puzzle_input)
    
    #prepare variables for iteration
    equal_match = []
    i = 0

    #iterate through a circular list of digits
    for current, nxt, mid in next_item(puzzle_digits):
        i += 1
        #check if current item is equal to next
        #if yes - add to matches list
        if matchtype == "nexts":
            if current == nxt:
                equal_match.append(int(current))
        #check if current item is equal to next
        #if yes - add to matches list
        if matchtype == "mids":
            if current == mid:
                equal_match.append(int(current))
        #since it's circular, it will never stop
        #iterating, remember to break when reaching
        #end of list
        if len(puzzle_digits) <= i:
            break
    #if no matches were found
    if equal_match == []:
        return 0
    else:
        #return the sum of all matches
        return(sum(equal_match))
