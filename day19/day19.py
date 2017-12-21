import os

FILENAME = os.path.join(os.path.dirname(__file__), 'input.txt')

def parse_input():
    with open(FILENAME) as f:
        rows = []
        for line in f.readlines():
            rows.append(line.strip('\n'))
        return rows

class Maze(object):
    def __init__(self, maze_map):
        self.maze_map = maze_map

    def get_location(self, coords):
        x, y = coords
        return self.maze_map[y][x]

    def coord_parse(self, coords):
        x = coords[0]
        y = coords[1]
        return x, y

    def is_valid_path(self, coords):
        if self.get_location(coords) != ' ':
            return True
        else:
            return False

    def is_turn(self, coords):
        x, y = coords
        if self.maze_map[y][x] == '+':
            return True
        else:
            return False

class MazeWalker(object):
    def __init__(self, maze):
        self.curr_pos = (63, 0)
        self.directions = ['N', 'E', 'S', 'W']
        self.curr_direction = self.directions[2]
        self.letters = []
        self.maze = maze
        self.steps = 0

    def move_offset(self):
        if self.curr_direction == 'N':
            return (0, -1)
        elif self.curr_direction == 'E':
            return (1, 0)
        elif self.curr_direction == 'S':
            return (0, 1)
        elif self.curr_direction == 'W':
            return (-1, 0)

    def next_coord(self):
        return tuple(map(sum, zip(self.curr_pos, self.move_offset())))

    def set_curr_pos(self, coords):
        self.curr_pos = coords
    
    def get_current_tile(self):
        return self.maze.get_location(self.curr_pos)

    def get_next_tile(self):
        return self.maze.get_location(self.next_coord())

    def check_path_valid(self):
        return self.maze.is_valid_path(self.next_coord())

    def check_path_turn(self, nxt=False):
        if not nxt:
            return self.maze.is_turn(self.curr_pos)
        else:
            return self.maze.is_turn(self.next_coord())
    
    def reverse_direction(self):
        i = self.directions.index(self.curr_direction)
        return self.directions[(i+2)%4]

    def change_direction(self, rev):
        i = self.directions.index(self.curr_direction)
        self.curr_direction = self.directions[(i+1)%4]
        if self.curr_direction == rev:
            self.change_direction(rev)

    def get_letter(self):
        s = self.get_current_tile()
        if s != ' ' and s != '+' and s != '-' and s != '|':
            self.letters.append(s)


    def move(self):
        rev = self.reverse_direction()
        if self.check_path_turn():
            while not self.check_path_valid():
                self.change_direction(rev)
                if self.check_path_turn(True):
                    self.change_direction(rev)
        
        if self.check_path_valid():
            self.set_curr_pos(self.next_coord())
        else: return "EOF"

    def traverse(self):
        self.get_letter()
        self.steps += 1
        return self.move()


maze = Maze(parse_input())
maze_walker = MazeWalker(maze)

while maze_walker.traverse() != "EOF":
    pass

print(maze_walker.curr_pos)
print(''.join(maze_walker.letters))
print(maze_walker.steps)