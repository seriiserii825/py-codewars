def descendingOrder(num):
    return int(''.join(sorted(str(num), reverse=True)))

print(descendingOrder(123456789)) # 987654321
