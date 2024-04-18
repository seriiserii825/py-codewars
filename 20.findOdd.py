def findOdd(seq):
    return [i for i in set(seq) if seq.count(i) % 2 != 0 ][0]

print(findOdd([1,1,4, 2, 2]))
