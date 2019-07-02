import itertools
import sys

per = [set() for i in range(10001)]
gyp = [set() for i in range(10001)]

def isquare (n):
    i = 1
    while i*i <= n:
        i <<= 1
    i >>= 1
    while i*i < n:
        i += 1
    return i*i == n

def wtf (p):
    q = p + 1
    p2 = p*p
    q2 = q*q
    while True:
        a = q2-p2
        b = 2*p*q
        if a > b:
            a, b = b, a
        c = q2+p2
        if c <= 10000:
            for i in range(1, 10000//c+1):
                gyp[i*c].add((a*i, b*i, c*i))
        else:
            break
        q += 1
        q2 = q*q

for i in range(1, 100):
    wtf(i)

for st in gyp[:]:
    ar = list(st)
    l = len(ar)
    if l >= 2:
        for index in itertools.combinations([i for i in range(l)], 2):
            cort1, cort2 = ar[index[0]], ar[index[1]]
            a = cort1[-1]
            if cort1[1] > cort2[1]:
                f, b = cort1[:-1]
                e, c = cort2[:-1]
            else:
                f, b = cort2[:-1]
                e, c = cort1[:-1]
            d2 = e*e-f*f
            if isquare(d2):
                x = (a*a+d2)/2
                if x == int(x):
                    print(int(x + a*a-x + b*b-x))
                    sys.exit(0)
