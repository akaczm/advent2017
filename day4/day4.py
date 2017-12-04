import itertools

def compare(a, b):
    if a == b:
        return True
    else:
        return False

def parse_input():
    with open('input.txt') as phrases:
        inputs = []
        for line in phrases:
            inputs.append(line)
        return inputs
    
def check_phrases():
    inputs = parse_input()
    valid = 0
    for line in inputs:
        words = line.split()
        if len(words) == len(set(words)):
            valid += 1
    
    print(valid)
    return valid

def check_anagram():
    inputs = parse_input()
    valid = 0
    for line in inputs:
        words = line.split()
        word_checksums = []
        for word in words:
            charlist = list(word)
            charset = set(charlist)
            word_checksum = {}
            for char in charset:
                word_checksum[char] = word.count(char)
            word_checksums.append(word_checksum)
        matches = []
        for a, b in itertools.combinations(word_checksums, 2):
            matches.append(compare(a, b))
        if matches.count(True) == 0:
            valid += 1
    
    print(valid)
        

check_phrases()
check_anagram()