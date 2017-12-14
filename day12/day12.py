import os
import re

REGEX_STR = r'^(?P<prog>\d+)\s<-> (?P<connection>.+)$'

class ProgramList(object):
    def __init__(self):
        self.programlist = []

    def __repr__(self):
        return str(self.programlist)

    def add_program(self, program):
        self.programlist.append(program)

    def get_program(self, id):
        if isinstance(id, Program):
            return id
        else:
            for program in self.programlist:
                if program.id == id:
                    return program

    def program_group(self, id, checked_list=[id]):
        program = self.get_program(id)
        group = [program]
        children = program.get_children()
        for child in children:
            child = self.get_program(child)
            group.append(child)
            self.get_descendants(checked_list, group, child)
        return set(group)

    def get_groups(self):
        checked_list = []
        groups = []
        for program in self.programlist:
            if program.id in checked_list:
                pass
            else:
                group = self.program_group(program, checked_list)
                groups.append(group)
        return groups

    def get_descendants(self, checked_list, group, child):
        children = child.get_children()
        for descendant in children:
            descendant = self.get_program(descendant)
            if descendant.id in checked_list:
                pass
            else:
                group.append(descendant)
                checked_list.append(descendant.id)
                self.get_descendants(checked_list, group, descendant)


class Program(object):    
    def __init__(self, id):
        self.id = id
        self.connected_to = []

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    def add_connection(self, ids):
        for id in ids:
            self.connected_to.append(id)

    def is_edge(self):
        if len(self.connected_to) == 1:
            return True
        else:
            return False

    def lookup_connection(self, id):
        for connection in self.connected_to:
            if connection == id:
                return True
            else: return False

    def get_children(self):
        return self.connected_to
    
            
def parse_input():
    FILENAME = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(FILENAME) as f:
        output = []
        p = re.compile(REGEX_STR)
        for line in f.readlines():
            match = p.match(line)
            output.append(match.groupdict())
        return output

def build_programlist(lst):
    programlist = ProgramList()
    for item in lst:
        id = int(item['prog'])
        connections = item['connection'].split(',')
        connections = list(map(str.strip, connections))
        connections = list(map(int, connections))
        program = Program(id)
        program.add_connection(connections)
        programlist.add_program(program)
    
    return programlist


programlist = build_programlist(parse_input())
grouped = programlist.program_group(0)
print(len(grouped))
groups = programlist.get_groups()
print(len(groups))

#Athalean's dank code
def get_connected_nodes_for(i):
    if i == 0:
        return [1, 2]
    if i == 1:
        return [2, 3]
    if i == 3:
        return [5]
    return []

visited = set()
group = set([0])
backlog = [0]
while backlog:
    print(backlog)
    current_node = backlog.pop(0)
    connected_nodes = set(get_connected_nodes_for(current_node))
    group |= connected_nodes
    backlog.extend(node for node in (connected_nodes - visited) if node not in backlog)
