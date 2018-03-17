def all_div (n) :
    d = set()
    for i in range(2, n+1) :
        if n % i == 0 :
            d = d.union({i})  
    return d
def all_prime_div (n) :
    d = set()
    while n > 1 :
        for i in range(2, n+1) :
            if n % i == 0  :
                d = d.union({i})
                n = n // i
                break
    return d

import euler
primelist = euler.primelist(100000)

def nprimediv (n) :
    c = 0
    sq = int(n**0.5)+1
    i = 0
    pr = primelist[0]
    while pr < sq :
        if not n % pr :
            c += 1
            while not n % pr :
                n //= pr
            sq = sq = int(n**0.5)+1
        i += 1
        pr = primelist[i]
    if n > 1 :
        c += 1
    return c



a1 = 1
a2 = 2
a3 = 3
a4 = 4
a = a4
d1 = nprimediv(a1)
d2 = nprimediv(a2)
d3 = nprimediv(a3)
d4 = nprimediv(a4)
while 1 :
    if d1 == 4 and d2 == 4 and d3 == 4 and d4 == 4 :
        print(a-3)
        break
    else :
        d1, d2, d3 = d2, d3, d4
        a += 1
        d4 = nprimediv(a)
