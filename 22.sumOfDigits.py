def digital_root(n):
    if n == 0:
        return 0
    total_sum = sum([int(i) for i in str(n)])
    return digital_root(total_sum) if len(str(total_sum)) > 1 else total_sum

print(f'digital_root(2489): {digital_root(248)}')
