import euler

def find (n) :
    rest = 1
    i = 1
    while rest :
        rest = (rest*10 + 1) % n
        i += 1
    return i

primelist = euler.primelist(100000)
primelist.remove(2)
primelist.remove(5)




res = 0
for pr in primelist :
    ff = f = find(pr)
    while f % 2 == 0 :
        f >>= 1
    while f % 5 == 0 :
        f //= 5
    if f == 1 :
        res += pr
print(sum(primelist)-res+2+5)
