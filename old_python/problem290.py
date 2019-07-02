
table = [str(i) for i in range(10)]+[chr(ord('a')+i) for i in range(20)]
def transform (n, base):
    power = base
    while power < n:
        power *= base
    res = ''
    while power:
        res += table[n//power]
        n %= power
        power //= base
    if res[0] != '0':
        return res
    return res[1:]


def digsum (n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res

for i in range(10000):
    if i % 9 == 0:
        if digsum(i) == digsum(i*137):
            print(i, digsum(i))
