import euler
import array



def M (p, q, n) : # p < q
    pr = p*q
    nq = 0
    while pr <= n :
        pr *= q
        nq += 1
    pr //= q
    while pr <= n :
        pr *= p
    pr //= p
    m = pr
    for i in range(nq-1) :
        pr //= q
        while pr <= n :
            pr *= p
        pr //= p
        if pr > m :
            m = pr
    return m

def S (n) :
    s = 0
    sq = int((n+1)**0.5)
    primelist = euler.primelist(n)
    prsq = euler.primelist(sq)
    for i in range(len(prsq)) :
        p = primelist[i]
        ind = i+1
        q = primelist[ind]
        while p*q <= n :
            m = M(p, q, n)
            s += m
            ind += 1
            q = primelist[ind]
    return s   
    
print(S(10*10**6))
