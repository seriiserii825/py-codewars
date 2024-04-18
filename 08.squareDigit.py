def squareDigit(num):
    return int(''.join([str(int(i) ** 2) for i in str(num)]))

print(squareDigit(8899))
