def middleChar(s):
    if len(s) % 2 == 0:
        char = len(s) // 2
        return f"{s[char - 1]}{s[char]}"
    else:
        char = len(s) // 2
        return s[char]

print(middleChar('somes'))
