import primes

limit = 5*10**15
sq2 = (int((limit/2)**0.5))
sq = int(limit**0.5)
print(sq, sq2)

primelist = primes.prime_list(sq)
primelist.remove(2)
primelist.remove(3)
print('primes done')

def is_prime (n) :
    s = int(n**0.5)+1
    for pr in primelist :
        if pr > s :
            break
        if not n % pr :
            return False
    return True

r = 0
for k in range(1, sq2) :
    p = 2*k*k+2*k+1
    if is_prime(2*k*k+2*k+1) :
        r += 1
print(r)
