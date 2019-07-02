import array
import sys
import math
import functools

sys.setrecursionLIMIT(10000)

def bn (n):
    return bin(n)[2:]

@functools.lru_cache(None)
def _calc (b):
    l = len(b)
    rf = b.rfind('1')
    if b.count('1') == 1:
        return l-rf
    return _calc(b[:rf])+(l-rf-1)*_calc(b[:rf]+'0')

@functools.lru_cache(None)
def calc (n):
    if n < 2:
        return 1
    if n & 1:
        return calc(n >> 1)
    r = 0
    while not n & 1:
        n >>= 1
        r += 1
    n >>= 1
    return calc(n) + r * calc(n << 1)

def wtf (j):
	i = 0
	while j > 2**i-1:
		i += 1
	return i

def first (j):
	return 2**wtf(j)+j

def second (j):
	return 2*2**wtf(j)+j

def pos (j, i):
    return 2**(wtf(j)+i)+j

def is_power2 (n):
    while not n & 1:
        n >>= 1
    return n == 1

def find (i, x, y):
    a = calc(first(i))
    b = calc(second(i)) - a
    c = calc(first(i + 1))
    d = calc(second(i + 1)) - c
    if is_power2(i + 1):
        c -= d
    num = c*x - a*y
    if num == 0:
        return 0.0
    denom = b*y - d*x
    if denom == 0:
        return -1
    return num / denom

def _SBE (n):
    temp = n & 1
    count = 0
    s = []
    while n:
        while n & 1 == temp:
            count += 1
            n >>= 1
        s = [count] + s
        temp = 1 - temp
        count = 0
    return s

def SBE (i, j):
    _ = _SBE(pos(i, 0) + 1)
    if j > 0:
        _[0] -= 1
        return '1,'+str(j) + ',' +','.join(str(s) for s in _)
    else:
        return ','.join(str(s) for s in _)

i = 0
x = 987654321
y = 123456789
#x, y = 17, 13
while True:
    f = find(i, x, y)
    if f >= 0.0:
        if f.is_integer():
            print(SBE(i, round(f)))
            break
    i += 1


if __name__ == '__main__':
    print(main())
