def multiply3or5(number):
    return sum([int(i) for i in range(number) if int(i) % 3 == 0 or int(i) % 5 == 0])

print(multiply3or5(6))
