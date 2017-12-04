from numpy import zeros, array


class ArrayTraverser(object):
    def __init__(self, arraysize):
        self.arraysize = arraysize
        self.numarray = zeros([arraysize, arraysize], dtype=int)
        self.center = int((arraysize + 1) / 2)
        self.sum = 0
        self.numarray[self.center][self.center] = 1
        self.current_loc = [self.center, self.center]
        self.direction = 'E'

    def move(self):
        if self.direction == 'E':
            self.current_loc[1] += 1

        elif self.direction == 'N':
            self.current_loc[0] -= 1

        elif self.direction == 'W':
            self.current_loc[1] -= 1

        elif self.direction == 'S':
            self.current_loc[0] += 1
    def scan_adjacent(self):
        self.sum = self.numarray[self.current_loc[0]][self.current_loc[1]] #C
        self.sum += self.numarray[self.current_loc[0]][self.current_loc[1] + 1] #E
        self.sum += self.numarray[self.current_loc[0] - 1][self.current_loc[1]] #N
        self.sum += self.numarray[self.current_loc[0] - 1][self.current_loc[1] +1] #NE
        self.sum += self.numarray[self.current_loc[0] - 1][self.current_loc[1] - 1] #NW
        self.sum += self.numarray[self.current_loc[0]][self.current_loc[1] - 1] #W
        self.sum += self.numarray[self.current_loc[0] + 1][self.current_loc[1] - 1] #SW
        self.sum += self.numarray[self.current_loc[0] + 1][self.current_loc[1]] #S
        self.sum += self.numarray[self.current_loc[0] + 1][self.current_loc[1] + 1] #SE
        self.numarray[self.current_loc[0]][self.current_loc[1]] = self.sum

    def change_direction(self):
        if self.direction == 'E' and self.numarray[self.current_loc[0] -1 ][self.current_loc[1]] == 0:
            self.next_direction()

        elif self.direction == 'N' and self.numarray[self.current_loc[0]][self.current_loc[1] -1] == 0:
            self.next_direction()

        elif self.direction == 'W' and self.numarray[self.current_loc[0] + 1][self.current_loc[1]] == 0:
            self.next_direction()

        elif self.direction == 'S'and self.numarray[self.current_loc[0]][self.current_loc[1] +1] == 0:
            self.next_direction()

    def next_direction(self):
        if self.direction == 'E':
            self.direction = 'N'

        elif self.direction == 'N':
            self.direction = 'W'

        elif self.direction == 'W':
            self.direction = 'S'

        elif self.direction == 'S':
            self.direction = 'E'

    def traverse(self):
        self.move()
        self.scan_adjacent()
        self.change_direction()
    
    def getcurrentvalue(self):
        return self.numarray[self.current_loc[0]][self.current_loc[1]]