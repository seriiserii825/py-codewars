def splitStrings(s):
    subarrays = [s[i:i+2] for i in range(0, len(s), 2)]
    return [i if len(i) == 2 else str(i) + '_' for i in subarrays]


print(splitStrings('abcdefgho'))

