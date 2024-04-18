def flickSwitch(arr):
    result, state = [], True
    for i in arr:
        if i == 'flick':
            state = not state
        result.append(state)
    return result


print(flickSwitch(['flick','sheep', 'flick', 'append', 'new', 'flick', 'second']))


