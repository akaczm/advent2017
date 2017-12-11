import os

class StreamSorter(object):
    
    def __init__(self, *args, **kwargs):
        self.stream = self.parse_input()
        self.is_garbage = False
        self.is_skip = False
        self.group = 0
        self.groupscore = 0
        self.sum_chars = 0

    @staticmethod
    def parse_input():
        FILENAME = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(FILENAME) as f:
            return f.read()

    def lookup_garbage(self, char):
        '''Check if stream is currently garbage'''
        if char == '<':
            self.is_garbage = True
            return True
        elif self.is_garbage and char == '>':
            self.is_garbage = False

    def is_skipped(self, char):
        '''Check if next char should be skipped'''
        if char =='!':
            self.is_skip = True
    
    def sum_group(self, val):
        self.groupscore += val

    def sum_garbage(self, char):
        if char == '>' or char == '!':
            pass
        else:
            self.sum_chars += 1

    def is_group(self, char):
        '''Check if it's a group open or close'''
        if char =='{':
            self.group += 1
            return True
        elif char =='}':
            self.sum_group(self.group)
            self.group -= 1

    def traverse_stream(self):
        for char in self.stream:
            if self.is_skip:
                self.is_skip = False
                continue
            self.is_skipped(char)
            if self.is_garbage is False:
                self.is_group(char)
            elif self.is_garbage:
                self.sum_garbage(char)
            self.lookup_garbage(char)
            



sorter = StreamSorter()
sorter.traverse_stream()
print(sorter.groupscore)
print(sorter.sum_chars)