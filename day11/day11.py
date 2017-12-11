import os
import operator

class HexTraverser(object):

    def __init__(self):
        self.path = self.parse_input()
        self.coords = (0, 0)
        self.origin = (0, 0)
        self.max_dist = (0, 0)
        self.max_steps = 0

    @staticmethod
    def parse_input():
        FILENAME = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(FILENAME) as f:
            content = f.read()
        return content.rstrip('\n').split(',')

    def reset(self):
        self.coords = (0, 0)

    def move(self, direction):
        if direction == 'n':
            self.coords = tuple(map(operator.add, self.coords, (-1, -1)))
        elif direction == 'ne':
            self.coords = tuple(map(operator.add, self.coords, (0, -1)))
        elif direction == 'se':
            self.coords = tuple(map(operator.add, self.coords, (1, 0)))
        elif direction == 's':
            self.coords = tuple(map(operator.add, self.coords, (1, 1)))
        elif direction == 'sw':
            self.coords = tuple(map(operator.add, self.coords, (0, 1)))
        elif direction == 'nw':
            self.coords = tuple(map(operator.add, self.coords, (-1, 0)))

    def final_coords(self):
        for direction in self.path:
            self.move(direction)
        return self.coords

    def furthest_coords(self):
        self.reset()
        for direction in self.path:
            self.move(direction)
            temp_coords = self.coords
            ret_steps = self.calculate_return()
            #if abs(self.coords[0]) + abs(self.coords[1]) > abs(self.max_dist[0]) + abs(self.max_dist[1]):
            #   self.max_dist = self.coords
            if ret_steps > self.max_steps:
                self.max_steps = ret_steps
                self.max_coords = temp_coords
            self.coords = temp_coords
        return (self.max_steps, self.max_coords)

    def calculate_return(self):
        steps = 0
        while (self.coords[0] is not 0 and self.coords[1] is not 0): #First go north or south
            print(self.coords)
            if self.coords[0] > self.origin[0]: #Origin is to the NW
                steps +=1
                self.move('n') 
            if self.coords[0] < self.origin[0]: #Origin is to the SE
                steps +=1
                self.move('s')

        while (self.coords[1] is not 0 or self.coords[0] is not 0): #go ne or sw as needed
            print(self.coords)
            if self.coords[1] is 0:
                if self.coords[0] > self.origin[0]:
                    steps +=1
                    self.move('nw') 
                if self.coords[0] < self.origin[0]:
                    steps +=1
                    self.move('se')
            elif self.coords[0] is 0:
                if self.coords[1] > self.origin[1]:
                    steps +=1
                    self.move('ne') 
                if self.coords[1] < self.origin[1]:
                    steps +=1
                    self.move('sw')
        return steps
        

hextraverser = HexTraverser()

hextraverser.final_coords()
print(hextraverser.furthest_coords())