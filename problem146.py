import euler

def qwerty (n) :
    nn = n*n
    i = 0
    pr = primelist[0]
    try : 
        while pr < n :
            bol = True
            for j in st :
                q = nn + j
                if not q % pr :
                    bol = False
                    break
            if not bol :
                break
            i += 1
            pr = primelist[i]
        if bol  :
            return n
        return 0
    except :
        return n

def cococo (n) :
    nn = n*n
    i = 0
    pr = primelist[0]
    while pr < n :
        bol = True
        for j in bad :
            q = nn + j
            if not q % pr :
                bol = False
                break
        if bol :
            break
        i += 1
        pr = primelist[i]
    if bol  :
        return n
    return 0

limit = 150*10**6

primelist = euler.primelist(100)
primelist.remove(2)
st = [1, 3, 7, 9, 13, 27]
bad = [5, 11, 15, 17, 19, 21, 23, 25]
ar = {2}
prod = 2
for pr in primelist :
    rest = set()
    
    for i in range(pr) :
        q = i*i
        bol = True
        for j in st :
            if not (q+j) % pr :
                bol = False
                break
        if bol :
            rest.add(i)
    
    newar = set()
    for a in ar :
        for i in range(pr) :
            q = a + prod*i
            if q < limit : 
                if q% pr in rest :
                    newar.add(q)
    ar = newar
    prod *= pr

primelist = euler.primelist(limit)



res = set()
for a in ar :
    if qwerty(a) :
        print(a)
        if not cococo(a) :
            res.add(a)
print(sum(res))
# without 676333270, because 676333270**2 - 23 is prime (it must not be prime)