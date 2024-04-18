def jadenCasing(string):
    return ' '.join(i.capitalize() for i in string.split())

print(jadenCasing("How can mirrors be real if our eYes aren't real"))
