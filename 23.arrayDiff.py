def arrayDiff(a, b):
    return [i for i in a if i not in b]

print(arrayDiff([1,2, 2], [1, 3, 4, 8]))
