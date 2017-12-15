
def valuegen(factor, startval, rng=1, div_by=1):
    nextval = (startval * factor) % 2147483647
    if nextval % div_by == 0:
        rng -= 1
        yield nextval
    for i in range(rng):
        nextval = (nextval * factor) % 2147483647
        while nextval % div_by != 0:
            nextval = (nextval * factor) % 2147483647
        yield nextval

def binarify(val):
    return bin(val).lstrip('-0b').zfill(32)

gen1 = valuegen(16807, 277, 5000000, 4)
gen2 = valuegen(48271, 349, 5000000, 8)
matches = 0
for val1, val2 in zip(gen1, gen2):
    bin1 = binarify(val1)[16:]
    bin2 = binarify(val2)[16:]
    if bin1 == bin2:
        matches += 1

print(matches)