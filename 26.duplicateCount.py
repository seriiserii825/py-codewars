def duplicateCount(text):
    return len([i for i in set(text.lower()) if text.lower().count(i) > 1])


print(duplicateCount(""))
print(duplicateCount("abcde"))
print(duplicateCount("abcdeaa"))
print(duplicateCount("abcdeaB"))
print(duplicateCount("Indivisibilities"))
