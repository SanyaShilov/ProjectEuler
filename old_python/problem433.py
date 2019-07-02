


def E (x, y):
    n = 0
    while y:
        x, y = y, x % y
        n += 1
    return n

LIMIT = 10000
'''
s = 0

m = [[0 for i in range(LIMIT+1)] for j in range(LIMIT+1)]
for i in range(1, LIMIT+1):
    for j in range(1, i):
        s += 2*E(i, j)
        m[i][j] = E(i, j)
print(s+LIMIT*(LIMIT+1)//2)
for k in m:
    print(k)'''
#
s = 0
sss = 0
for j in range(1, LIMIT//2):
    sm = 0
    if not j % 1000:
        print(j)
    j2 = j+j
    r = LIMIT - j2
    stop = r % j + 1
    for i in range(1, j+1):
        sm += E(i, j)
        if i < stop:
            s += E(i, j)
    s += sm*(r//j)
n = LIMIT
print(s)
print(4*s+n*n//2+n*(n+1)//2)
