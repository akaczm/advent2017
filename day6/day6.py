from itertools import cycle, islice
from timeit import default_timer as timer

def parse_input():
    with open('input.txt') as numbers:
        splitnums = numbers.readline().split()
        splitnums = list(map(int, splitnums))
        return splitnums

def reallocate():
    start = timer()
    nums = parse_input()
    print(nums)
    membanks = len(nums)
    arrangements = []
    arrangements.append(tuple(nums))
    i = 0
    currentnums = nums
    lastarrangement = 0
    while len(arrangements) == len(set(arrangements)):
        i += 1
        maxitems = currentnums.index(max(currentnums))
        redist = currentnums[maxitems] # memory to redistribute
        currentnums[maxitems] -= redist
        index = maxitems + 1
        while redist > 0:  
            redist -= 1
            currentnums[index % len(currentnums)] += 1
            index += 1
        arrangements.append(tuple(currentnums))
        lastarrangement = tuple(currentnums)

    print(abs(arrangements.index(lastarrangement) - i))
    print(i)
    end = timer()
    print (end - start)

reallocate()