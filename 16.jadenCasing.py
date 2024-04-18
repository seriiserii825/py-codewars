def jadenCasing(string):
    return ' '.join(i[0].upper() + i[1:] for i in string.lower().split())

print(jadenCasing("How can mirrors be real if our eyes aren't real"))
