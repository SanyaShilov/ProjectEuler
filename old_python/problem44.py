import sys

def penta (n):
    return n*(3*n-1)//2

def is_penta (n):
    a = (1+(1+24*n)**0.5)/6
    return round(a) == round(a, 7)

p = [penta(i) for i in range(100000)]

for k in range(1, 100000):
    pk = p[k]
    for j in range(1, k):
        pj = p[j]
        if is_penta(pk-pj):
            if is_penta(pk+pj):
                print(pk-pj)
                sys.exit(0)
