import primes
primelist = primes.prime_list(10**4)

def fi (n) :
    nn = (n+1)//2
    res = n-1
    for pr in primelist :
        if pr > nn :
            break
        if not n % pr :
            res -= res//pr
    return res

def hyperpower (a, b, c) :
    r = 1
    while b :
        r = (r*a)%c
        b -= 1
    return r

def hyper (a, b, c) :
    print('called hyper with', a, b, c)
    if b == 1 :
        return a%c
    if c == 2 :
        return a%2
    res = hyperpower(a, (hyper(a, b-1, fi(c))), c)
    print('returned' ,res)
    return res


print(hyper(1777, 1855, 10**8))
