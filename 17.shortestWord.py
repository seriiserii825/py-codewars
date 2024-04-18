def shortestWord(s):
    return min(len(i) for i in s.split())

print(shortestWord('a some word for me'))
