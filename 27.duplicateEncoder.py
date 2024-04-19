def duplicate_encode(word):
    word = word.lower()
    return ''.join(['(' if word.count(i) == 1 else ')'  for i in word])

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
