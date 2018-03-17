from fractions import *
from itertools import *
from functools import *


class MyFraction :
    def __init__ (self, a, b = 1) :
        self.a = a
        self.b = b
    def __add__ (self, other) :
        return MyFraction(self.a*other.b + self.b*other.a, self.b*other.b)
    def __sub__ (self, other) :
        return MyFraction(self.a*other.b - self.b*other.a, self.b*other.b)
    def __mul__ (self, other) :
        return MyFraction(self.a*other.a, self.b*other.b)
    def __truediv__ (self, other) :
        return MyFraction(self.a*other.b, self.b*other.a)
    def __hash__ (self) :
        return hash(self.a/self.b)
    def __eq__ (self, other) :
        return self.a/self.b == other.a/other.b
    

def two_comb (a, b) :
    if type(a) == str :
        if type(b) == str :
            sa = int(a)
            sb = int(b)
            sab = a+b
            return {(sa+sb), (sa-sb), (sa*sb), (sa/sb), sab}
        sa = int(a)
        if b :
            return {(sa+b), (sa-b), (sa*b), (sa/b)}
        return {(sa), (0)}
    if type(b) == str :
        sb = int(b)
        return {(a+sb), (a-sb), (a*sb), (a/sb)}
    if b :
        return {(a+b), (a-b), (a*b), (a/b)}
    return {(a), 0}

def two_comb (a, b) :
    if type(a) == str :
        if type(b) == str :
            sa = MyFraction(int(a))
            sb = MyFraction(int(b))
            sab = a+b
            return {(sa+sb), (sa-sb), (sa*sb), (sa/sb), sab}
        sa = MyFraction(int(a))
        if b.a :
            return {(sa+b), (sa-b), (sa*b), (sa/b)}
        return {(sa), MyFraction(0)}
    if type(b) == str :
        sb = MyFraction(int(b))
        return {(a+sb), (a-sb), (a*sb), (a/sb)}
    if b.a :
        return {(a+b), (a-b), (a*b), (a/b)}
    return {(a), MyFraction(0)}

def multi_comb (ar) :
    l = len(ar)
    if l == 1 :
        return {ar[0]}
    if l == 2 :
        return two_comb(ar[0], ar[1])
    res = set()
    for i in range(1, l) :
        m1 = multi_comb(ar[:i])
        m2 = multi_comb(ar[i:])
        for a in m1 :
            for b in m2 :
                res.update(two_comb(a, b))
    return res

m = multi_comb([str(i) for i in range(1, 9+1)])
print('len', len(m))

s = set()
for k in m :
    if type(k) == str :
        k = MyFraction(int(k))
    if k.a * k.b > 0 :
        if not k.a % k.b :
            s.add(k.a//k.b)
print('sum', sum(s))

'''
n = 6

f = [[set() for i in range(n + 1)] for j in range(n + 1)]

for l in reversed(range(n + 1)):
    for r in range(l + 1, n + 1):
        tmp = [Fraction(reduce(lambda x, y: x * 10 + y, range(1, n + 1)[l:r]))]
        for k in range(l, r):
            for a in f[l][k]:
                for b in f[k][r]:
                    tmp += [a + b]
                    tmp += [a - b]
                    tmp += [a * b]
                    if b != 0:
                        tmp += [a / b]

        f[l][r] = set(tmp)

ans = 0
for v in f[0][n]:
    if v == int(v) and v > 0:
        ans += int(v)
print ('ans = %d' % ans)
'''