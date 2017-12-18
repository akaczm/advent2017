import os

SAMPLE_INPUT = 's1, x3/4, pe/b'
split_input = list(map(str.strip, SAMPLE_INPUT.split(',')))

FILENAME = os.path.join(os.path.dirname(__file__), 'input.txt')
def parse_input(filename):
    with open(filename) as f:
        inpt = f.read()
        return list(map(str.strip, inpt.split(',')))

proglist = list(map(chr, range(97, 113)))
startlist = list(map(chr, range(97, 113)))
testlist = list(map(chr, range(97, 102)))

def dance(input, proglist):
    for item in input:
        if item[:1] == 's':
            spin(item[1:], proglist)
        else:
            swap(item[1:], proglist)

def spin(vals, proglist):
    val = int(vals)
    proglist[:] = proglist[-val:] + proglist[:-val]

def swap(vals, proglist):
    val1, val2 = vals.split('/')
    try:
        val1 = int(val1)
        val2 = int(val2)
        proglist[val1], proglist[val2] = proglist[val2], proglist[val1]
    except ValueError:
        val1, val2 = proglist.index(val1), proglist.index(val2)
        proglist[val1], proglist[val2] = proglist[val2], proglist[val1]

def calc_changes(proglist, startlist):
    changed_indices = []
    for item in startlist:
        changed_indices.append(proglist.index(item))
    return changed_indices

def permutate(proglist, changes):
    cached_list = list(proglist)
    x = 0
    for i in changes:
        proglist[i] = cached_list[x]
        x += 1


moves = parse_input(FILENAME)
i = 0
while i < 1000:
    i += 1
    if i % 100 == 0:
        print(i)
    dance(moves, proglist)
    
changes = calc_changes(proglist, startlist)

while i < 1000000000:
    permutate(proglist, changes)
    i += 1000

print(i)
print(''.join(proglist))

#dance(split_input, testlist)