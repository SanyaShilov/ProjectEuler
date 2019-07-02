import primes

prime_list = primes.prime_list(1000)
'''
s = set()
last = 10**200
big = 10**100
for a in range(2, 1000000):
    if not a % 1000:
        print(a)
        if len(s) > 150000:
            last = big
            big = sorted(list(s))[149999]
            print(big)
            if big == last:
                print('big', big)
    ar = [True for i in range(a)]
    i = 0
    pr = prime_list[0]
    stop = int(a**0.5)
    while pr <= stop:
        if not a % pr:
            for j in range(pr, a, pr):
                ar[j] = False
            n = a//pr
            for j in range(n, a, n):
                ar[j] = False
        i += 1
        pr = prime_list[i]
    for b in range(1, a):
        if ar[b]:
            q = a*b + 1
            w = a-b
            if not q % w:
                A = a*b*q//w
                if A > big:
                    break
                s.add(A)
print(len(s))
'''

s = set()
big = 2780327961486396
big = 2162524708409208
big = 1924468502360166
big = 1890731004516726
big = 1885521049569234
big = 1884283330430556
big = 1884161251122450
for d in range(1, 1000000):
    if d % 100 == 0:
        print(d, len(s))
        if len(s) > 150000:
            last = big
            big = sorted(list(s))[150000]
            print(big)
            if big == last:
                print('big', big)
                break
    rest = []
    for r in range(d-1, -1, -1):
        if not (r*r+1) % d:
            rest.append(r)
    if not rest:
        continue
    start = 0
    while True:
        for r in rest:
            b = start + r
            a = b + d
            A = a*b*(a*b+1)//d
            s.add(A)
        if A > big:
            break
        start += d
    
    
ar = sorted(list(s))
print(len(ar))
print(ar[:12])
