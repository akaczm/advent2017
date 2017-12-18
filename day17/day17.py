from itertools import cycle

val_list = [0]
step = 343
insertions = 2017

def step_through(val_list, step, curr_pos=0, n=1):
    i = 0
    cyc = cycle(val_list)
    next(cyc)
    while i < step:
        if curr_pos != 0:
            while curr_pos > 0:
                curr_pos -= 1
                next(cyc)
        nextval = next(cyc)
        i += 1
    index = val_list.index(nextval)
    val_list.insert(index+1, n)
    return index+1, n+1

def spinlock(val_list, step, insertions, p2=False):
    curr_pos = 0
    n = 1
    if not p2:
        while insertions > 0:
            insertions -= 1
            curr_pos, n = step_through(val_list, step, curr_pos, n)
    else:
        for i in range(1,50000001):
            curr_pos = (curr_pos+step)%i+1
            if curr_pos==1:
                final = i
        return(final) 

#part1 solution
#spinlock(val_list, step, insertions)

#part2 solution
print(spinlock(val_list,step, insertions, True))
