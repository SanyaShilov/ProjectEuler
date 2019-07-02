#


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

s = 16
last = [7, 8]
lastsum = [7, 8]
LIMIT = 14
add = 1
two = 2
for n in range(2, 10001):
    newlast = []
    newlastsum = []
    LIMIT *= 14
    add *= 14
    two <<= 1
    for k in range(len(last)):
        start = last[k]
        dig = 0
        while start < LIMIT:
            if not (start-1)*start % LIMIT:
                newlast.append(start)
                sm = lastsum[k]+dig
                if dig:
                    s += sm
                newlastsum.append(sm)
                break
            start += add
            dig += 1
    last = newlast
    lastsum = newlastsum
print(transform(s, 14))


if __name__ == '__main__':
    print(main())
