def parse_input():
    with open('input.txt') as numbers:
        inputs = []
        for line in numbers:
            inputs.append(int(line))
        return inputs

def traverse_maze_p1():
    maze = parse_input()
    i = 0
    steps = 0
    while True:
        try:
            step = maze[i]
            maze[i] += 1
            i += step
            steps += 1
        except IndexError:
            print(steps)
            return steps

def traverse_maze_p2():
    maze = parse_input()
    i = 0
    steps = 0
    while True:
        try:
            step = maze[i]
            if maze[i] >= 3:
                maze[i] -= 1
            else: maze[i] += 1
            i += step
            steps += 1
        except IndexError:
            print(steps)
            return steps           
            

traverse_maze_p1()
traverse_maze_p2()