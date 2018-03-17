import euler

primelist = euler.primelist(100000)

def is_prime (n) :
    for i in range(2, int(n**0.5)+1) :
        if n % i == 0 :
            return False
    return True

ar = [i for i in range(10000)]
for i in range(2, 100) :
    for j in range(2, 10000 // i + 100) :
        try :
            ar[i*j] = 0
        except :
            pass

for i in range(3, 10000) :
    if ar[i] != 0 :
        li = len(str(i))
        li10 = 10**li
        for j in range(i, 10000) :
            if ar[j] != 0 :
                if euler.isprime(j*li10+i, primelist) :
                    lj = len(str(j))
                    lj10 = 10**lj
                    if euler.isprime(i*lj10+j, primelist) :
                        for k in range(j, 10000) :
                            if ar[k] != 0 :
                                if euler.isprime(k*li10+i, primelist) :
                                    if euler.isprime(k*lj10+j, primelist) :
                                        lk = len(str(k))
                                        lk10 = 10**lk
                                        if euler.isprime(i*lk10+k, primelist) :
                                            if euler.isprime(j*lk10+k, primelist) :
                                                for q in range(k, 10000) :
                                                    if ar[q] != 0 :
                                                        if euler.isprime(q*li10+i, primelist) :
                                                            if euler.isprime(q*lj10+j, primelist) :
                                                                if euler.isprime(q*lk10+k, primelist) :
                                                                    lq = len(str(q))
                                                                    lq10 = 10**lq
                                                                    if euler.isprime(i*lq10+q, primelist) :
                                                                        if euler.isprime(j*lq10+q, primelist) :
                                                                            if euler.isprime(k*lq10+q, primelist) :
                                                                                for w in range(q, 10000) :
                                                                                    if ar[w] != 0 :
                                                                                        if euler.isprime(w*li10+i, primelist) :
                                                                                            if euler.isprime(w*lj10+j, primelist) :
                                                                                                if euler.isprime(w*lk10+k, primelist) :
                                                                                                    if euler.isprime(w*lq10+q, primelist) :
                                                                                                        lw = len(str(w))
                                                                                                        lw10 = 10**lw
                                                                                                        if euler.isprime(i*lw10+w, primelist) :
                                                                                                            if euler.isprime(j*lw10+w, primelist) :
                                                                                                                if euler.isprime(k*lw10+w, primelist) :
                                                                                                                    if euler.isprime(q*lw10+w, primelist) :
                                                                                                                        s = {i, j, k, q, w}
                                                                                                                        print(sum(s))
                                                                                                                        exit()
       





# 13 + 5701 + 8389 + 6733 + 5197 = 26033 !!!










                    
