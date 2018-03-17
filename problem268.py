import euler
import itertools

limit = 10**16

primelist = euler.primelist(100)

def product (ar) :
    a = 1
    for i in ar :
        a *= i
    return a
'''
s = set()
l = 0
for c in itertools.combinations(primelist, 4) :
    l += 1
    a = product(c)
    for i in range(a, limit, a) :
        s.add(i)
print(len(s))
'''

s = 0
l = 0
for c in itertools.combinations(primelist, 4) :
    l += 1
    if not l % 100 :
        print(l)
    ar = []
    m = c[-1]
    for pr in primelist :
        if pr < m and pr not in c :
            ar.append(pr)
    a = 1
    for pr in c :
        a *= pr
    s += euler.notdivisible(limit//a, ar, len(ar))
print(s)
