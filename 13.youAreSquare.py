def youAreSquare(n):
    return True if n >= 0 and int(n ** 0.5) == n ** 0.5 else False

print(youAreSquare(25))
