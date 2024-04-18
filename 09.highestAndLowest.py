def highestAndLowest(numbers):
    result = sorted([int(x) for x in numbers.split()])
    return f'{result[len(result) - 1]} {result[0]}'

print(highestAndLowest('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))
