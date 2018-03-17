def fact (n) :
    r = 1
    while n > 1 :
        r = r * n
        n -= 1
    return r

tab = [fact(i) for i in range(101)]
s = 0
for n in range (1, 101) :
    for r in range(n+1) :
        if tab[n] / tab[r] / tab[n-r] > 1000000 :
            s += 1
print(s)
