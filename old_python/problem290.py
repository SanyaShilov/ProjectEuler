
table = [str(i) for i in range(10)]+[chr(ord('a')+i) for i in range(20)]
def transform (n, base):
    power = base
    while power < n:
        power *= base
    result = ''
    while power:
        result += table[n//power]
        n %= power
        power //= base
    if result[0] != '0':
        return result
    return result[1:]


def digsum (n):
    result = 0
    while n:
        result += n % 10
        n //= 10
    return result

for i in range(10000):
    if i % 9 == 0:
        if digsum(i) == digsum(i*137):
            print(i, digsum(i))
