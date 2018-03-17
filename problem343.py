import primes

def max_delimiter (n) :
    i = 0
    pr = primelist[0]
    sq = (n+1)**0.5
    while pr < sq :
        if n % pr == 0 :
            n //= pr
            sq = (n+1)**0.5
            i -= 1
        i += 1
        pr = primelist[i]
    return n

def calc (n) :
    nn = n+1
    i = 0
    pr = primelist[0]
    sq = (nn+1)**0.5
    while pr < sq :
        if nn % pr == 0 :
            nn = nn//pr
            sq = (nn+1)**0.5
            i = -1
        i += 1
        pr = primelist[i]
    return nn-1

def calc (n) :
    return max_delimiter(n+1)

def cubcalc (n) :
    num = n*n-n+1
    m = max_delimiter(num)
    if m > max_delimiter(n+1) :
        return m-1
    return n

l = 2000001
primelist = primes.prime_list(l+1)

'''
car = [calc(i) for i in ar]
print(car)
print(sum(car)-101)
'''
ar = [i*i*i + 1 for i in range(l)]

for pr in primelist :
    print(pr)
    for j in range(1, pr) :
        if ar[j] % pr == 0:
            for i in range(j, l, pr) :
                while pr < ar[i] :
                    if ar[i] % pr == 0 :
                        ar[i] //= pr
                    else :
                        break
                
print(sum(ar)-l)
'''
print(len(primelist))

s = 0
for i in range(1, 2*10**6+1) :
    if i % 1000 == 0 :
        print(i)
    s += cubcalc(i)
print(s)
'''
