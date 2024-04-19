def phoneNumber(n):
    n = ''.join(map(str, n))
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"

print(phoneNumber([1,2,3,4,5,6,7,8,9,0]))
