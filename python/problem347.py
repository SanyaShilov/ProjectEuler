import euler
import array



def M (p, q, n): # p < q
    pr = p*q
    nq = 0
    while pr <= n:
        pr *= q
        nq += 1
    pr //= q
    while pr <= n:
        pr *= p
    pr //= p
    m = pr
    for i in range(nq-1):
        pr //= q
        while pr <= n:
            pr *= p
        pr //= p
        if pr > m:
            m = pr
    return m

def S (n):
    s = 0
    sq = int((n+1)**0.5)
    prime_list = euler.prime_list(n)
    prsq = euler.prime_list(sq)
    for i in range(len(prsq)):
        p = prime_list[i]
        ind = i+1
        q = prime_list[ind]
        while p*q <= n:
            m = M(p, q, n)
            s += m
            ind += 1
            q = prime_list[ind]
    return s   
    
print(S(10*10**6))


if __name__ == '__main__':
    print(main())
