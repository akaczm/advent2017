import csv

def parse_input():
    with open('input.txt') as tsv:
        inputs = []
        for line in csv.reader(tsv, delimiter='\t'):
            inputs.append(list(map(int, line)))
        
        return inputs

def check_divis(row):
    result = 0
    for item in row:
        for i in range(len(row)):
            divisible = item % row[i]
            if divisible == 0 and item != row[i]:
                result += item / row[i]
    return result
    

def calculate_checksum_minmax(inpt):
    checksum = 0
    for row in inpt:
        checksum += (max(row) - min(row))
    print(checksum)
    return checksum

def calculate_checksum_divis(inpt):
    checksum = 0
    for row in inpt:
        checksum += check_divis(row)
    print(checksum)

calculate_checksum_divis(parse_input())