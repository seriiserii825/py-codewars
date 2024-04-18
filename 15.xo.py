def xo(s):
    return s.lower().count('x') == s.lower().count('o') 

print(xo('xoxoXo'))
print(xo('xoxxo'))
