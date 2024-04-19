def unique_in_order(sequence):
    unique = None
    result = []
    for i in sequence:
        if i != unique:
            result.append(i)
            unique = i
    return result

print(unique_in_order(['a', 'a', 'b', 'c', 'c']))
print(unique_in_order([1, 2, 3, 3, -1]))
print(unique_in_order(["a", "b", "b", "a"]))
        
