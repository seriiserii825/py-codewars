def sort_array(source_array):
    result = source_array[:]
    odd = [i for i in source_array if i % 2 != 0]
    odd.sort()
    start_index = 0
    for index, i in enumerate(source_array):
        if i % 2 != 0:
            del(result[index])
            result.insert(index, odd[start_index])
            start_index += 1
    return result
print(sort_array([8, 5, 0, 3, 22, 1, 44, 4]))
