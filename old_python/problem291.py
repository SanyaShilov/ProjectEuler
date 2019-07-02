import euler

LIMIT = 5*10**8
sq2 = (int((LIMIT/2)**0.5))
sq = int(LIMIT**0.5)
print(sq, sq2)

prime_list = euler.prime_list(sq)
prime_list.remove(2)
prime_list.remove(3)
print('primes done')

def is_prime (n):
    s = int(n**0.5)+1
    for pr in prime_list:
        if pr > s:
            break
        if not n % pr:
            return False
    return True

r = 0
for k in range(1, sq2):
    p = 2*k*k+2*k+1
    if is_prime(2*k*k+2*k+1):
        r += 1
print(r)
