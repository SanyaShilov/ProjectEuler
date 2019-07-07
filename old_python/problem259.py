from fractions import *
from itertools import *
from functools import *


class MyFraction:
    __slots__ = ('a', 'b')
    def __init__ (self, a, b = 1):
        self.a = a
        self.b = b
    def __add__ (self, other):
        return MyFraction(self.a*other.b + self.b*other.a, self.b*other.b)
    def __sub__ (self, other):
        return MyFraction(self.a*other.b - self.b*other.a, self.b*other.b)
    def __mul__ (self, other):
        return MyFraction(self.a*other.a, self.b*other.b)
    def __truediv__ (self, other):
        return MyFraction(self.a*other.b, self.b*other.a)
    def __hash__ (self):
        return hash(self.a/self.b)
    def __eq__ (self, other):
        return self.a/self.b == other.a/other.b
    

def two_comb (a, b):
    if type(a) == str:
        if type(b) == str:
            sa = int(a)
            sb = int(b)
            sab = a+b
            return {(sa+sb), (sa-sb), (sa*sb), (sa/sb), sab}
        sa = int(a)
        if b:
            return {(sa+b), (sa-b), (sa*b), (sa/b)}
        return {(sa), (0)}
    if type(b) == str:
        sb = int(b)
        return {(a+sb), (a-sb), (a*sb), (a/sb)}
    if b:
        return {(a+b), (a-b), (a*b), (a/b)}
    return {(a), 0}

def two_comb (a, b):
    if type(a) == str:
        if type(b) == str:
            sa = MyFraction(int(a))
            sb = MyFraction(int(b))
            sab = a+b
            return {(sa+sb), (sa-sb), (sa*sb), (sa/sb), sab}
        sa = MyFraction(int(a))
        if b.a:
            return {(sa+b), (sa-b), (sa*b), (sa/b)}
        return {(sa), MyFraction(0)}
    if type(b) == str:
        sb = MyFraction(int(b))
        return {(a+sb), (a-sb), (a*sb), (a/sb)}
    if b.a:
        return {(a+b), (a-b), (a*b), (a/b)}
    return {(a), MyFraction(0)}

def multi_comb (lst):
    l = len(lst)
    if l == 1:
        return {lst[0]}
    if l == 2:
        return two_comb(lst[0], lst[1])
    result = set()
    for i in range(1, l):
        m1 = multi_comb(lst[:i])
        m2 = multi_comb(lst[i:])
        for a in m1:
            for b in m2:
                result.update(two_comb(a, b))
    return result

m = multi_comb([str(i) for i in range(1, 9+1)])
print('len', len(m))

s = set()
for k in m:
    if type(k) == str:
        k = MyFraction(int(k))
    if k.a * k.b > 0:
        if not k.a % k.b:
            s.add(k.a//k.b)
print('sum', sum(s))
