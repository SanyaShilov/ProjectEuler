import sys
import euler


ANSWER =


prime_list = euler.prime_list(1000000)

def is_prime (n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

lst = [i for i in range(10000)]
for i in range(2, 100):
    for j in range(2, 10000 // i + 100):
        try:
            lst[i*j] = 0
        except:
            pass



for i in range(3, 10000):
    if lst[i] != 0:
        li = len(str(i))
        li10 = 10**li
        for j in range(i, 10000):
            if lst[j] != 0:
                if euler.is_prime(j*li10+i, prime_list):
                    lj = len(str(j))
                    lj10 = 10**lj
                    if euler.is_prime(i*lj10+j, prime_list):
                        for k in range(j, 10000):
                            if lst[k] != 0:
                                if euler.is_prime(k*li10+i, prime_list):
                                    if euler.is_prime(k*lj10+j, prime_list):
                                        lk = len(str(k))
                                        lk10 = 10**lk
                                        if euler.is_prime(i*lk10+k, prime_list):
                                            if euler.is_prime(j*lk10+k, prime_list):
                                                for q in range(k, 10000):
                                                    if lst[q] != 0:
                                                        if euler.is_prime(q*li10+i, prime_list):
                                                            if euler.is_prime(q*lj10+j, prime_list):
                                                                if euler.is_prime(q*lk10+k, prime_list):
                                                                    lq = len(str(q))
                                                                    lq10 = 10**lq
                                                                    if euler.is_prime(i*lq10+q, prime_list):
                                                                        if euler.is_prime(j*lq10+q, prime_list):
                                                                            if euler.is_prime(k*lq10+q, prime_list):
                                                                                for w in range(q, 10000):
                                                                                    if lst[w] != 0:
                                                                                        if euler.is_prime(w*li10+i, prime_list):
                                                                                            if euler.is_prime(w*lj10+j, prime_list):
                                                                                                if euler.is_prime(w*lk10+k, prime_list):
                                                                                                    if euler.is_prime(w*lq10+q, prime_list):
                                                                                                        lw = len(str(w))
                                                                                                        lw10 = 10**lw
                                                                                                        if euler.is_prime(i*lw10+w, prime_list):
                                                                                                            if euler.is_prime(j*lw10+w, prime_list):
                                                                                                                if euler.is_prime(k*lw10+w, prime_list):
                                                                                                                    if euler.is_prime(q*lw10+w, prime_list):
                                                                                                                        s = {i, j, k, q, w}
                                                                                                                        print(sum(s))
                                                                                                                        sys.exit()


# 13 + 5701 + 8389 + 6733 + 5197 = 26033 !!!


if __name__ == '__main__':
    print(main())
