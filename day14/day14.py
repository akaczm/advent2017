from day10.day10 import calc_hash

def generate_hashes(string):
    '''generate hashes based off input string'''
    return [bin(int(calc_hash((string + '-' + str(i))), 16)).lstrip('-0b').zfill(128)
            for i in range(128)]

def calc_groups(hashlist):
    i = 0
    grouped = []
    for y, row in enumerate(hashlist):
        for x, item in enumerate(row):
            if item == '0' or (x,y) in grouped:
                continue
            res, i = check_adjacency(hashlist, (x, y), grouped, group=i)
    return grouped, i

def check_adjacency(grid, coords, grouped=[], group=1, rec=False):
    x, y = coords
    matched = False
    curr_group = group
    try:
        if (grid[y][x+1] == '1') and ((x+1, y) not in grouped):
            matched = True
            grouped.append((x+1, y))
            check_adjacency(grid, (x+1, y), grouped, rec=True)
    except IndexError:
        pass
    if grid[y][x-1] == '1' and x-1 != -1 and (x-1, y) not in grouped:
        matched = True
        grouped.append((x-1, y))
        check_adjacency(grid, (x-1, y), grouped, rec=True)
    try:
        if grid[y+1][x] == '1' and (x, y+1) not in grouped:
            matched = True
            grouped.append((x, y+1))
            check_adjacency(grid, (x, y+1), grouped, rec=True)
    except IndexError:
        pass
    if grid[y-1][x] == '1' and y-1 != -1 and (x, y-1) not in grouped:
        matched = True
        grouped.append((x, y-1))
        check_adjacency(grid, (x, y-1), grouped, rec=True)
    
    if not matched:
        if not rec:
            grouped.append((x,y))
            return grouped, curr_group+1
        else:
            return grouped, curr_group

    return grouped, curr_group+1

hashlist = generate_hashes('jxqlasbh')
result = 0
for hsh in hashlist:
    result += str(hsh).count('1')
grouped, groups = calc_groups(hashlist)
print(groups)