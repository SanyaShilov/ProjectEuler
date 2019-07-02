def fact (n):
    r = 1
    while n > 1:
        r *= n
        n -= 1
    return r

for i in range(2, 55):
    print(str(hex(fact(i)))[-30:])
