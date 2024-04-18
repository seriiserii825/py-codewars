def isogram(string):
    return len(string) == len(set(string.lower()))

print(isogram('mose'))
