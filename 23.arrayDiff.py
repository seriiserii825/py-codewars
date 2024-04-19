def arrayDiff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)

    return result

print(arrayDiff([1,2, 2], [1, 3, 4, 8]))
