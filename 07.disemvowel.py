def disemvowel(string):
    return ''.join([i if i.lower() not in 'aeiou' else '' for i in string])

print(disemvowel('This website is for losers LOL!'))
