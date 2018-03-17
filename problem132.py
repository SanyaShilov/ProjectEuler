import euler

def find (n) :
    rest = 1
    i = 1
    while rest :
        rest = (rest*10 + 1) % n
        i += 1
    return i


primelist = euler.primelist(1000000)
primelist.remove(2)
primelist.remove(5)


s = 0
big = 10**9
count = 0
for pr in primelist :
        if big % find(pr) == 0 :
            count += 1
            s += pr
            if count == 40 :
                break
print(s)

