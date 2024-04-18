def vowelCount(sentence):
    volves = 'aeiou'
    return sum([sentence.count(i) for i in volves])

print(vowelCount('some string for me'))
