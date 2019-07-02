def div (n):
    d = set()
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                d = d.union({i})
                n = n // i
                break
    return d

def fract (n):
    s = 0
    dn = div(n)
    for i in range(n//3 + 1, (n+1)//2):
        for d in dn:
            if i % d == 0:
                break
        else:
            s += 1
    return s

s = 0
for i in range(2, 12001):
    s += fract(i)
print(s)
