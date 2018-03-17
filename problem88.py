def product (ar) :
    a = 1
    for k in ar :
        a *= k
    return a


def find(k, n, ar, ind) :
    s = sum(ar)+k-n
    p = product(ar)
    if p == s :
        return s
    if p > s :
        return big
    if ind == n :
        return big
    
    

def mnm (k) :
    s = k
    pr = 1
    n = 0
    while s > pr :
        s += 1
        pr <<= 1
        n += 1
    for i in range(2, n) :
        find(k, i, [2 for i in range(n)], 0)
    print(pr, s, n)




big = 10**10

limit = 120

solve = [big for i in range(limit+1)]

aar = []
sums = []
lens = []

for i in range(2, 15) :
    aar.append([2 for j in range(i)])
    sums.append(2*i)
    lens.append(i)

n = 1
while aar :
    if not n % 1000000 :
        print(n)
    n += 1
    ar = aar.pop()
    l = lens.pop()
    s = sums.pop()
    p = product(ar)
    psl = p - s + l
    if psl <= limit :
        s1 = s + 1
        ss = solve[psl]
        if ss > p :
            solve[psl] = p
        new = ar[:]
        new[-1] += 1
        aar.append(new)
        sums.append(s1)
        lens.append(l)
        for i in range(len(ar)-1) :
            if ar[i] < ar[i+1] :
                new = ar[:]
                new[i] += 1
                aar.append(new)
                sums.append(s1)
                lens.append(l)
print(sum(set(solve[2:])))

