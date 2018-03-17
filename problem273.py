import primes

primelist = primes.prime_list(150)

s = 0
p = 1
for pr in primelist :
    if pr % 4 == 1 :
        print(pr)
        p *= pr
        s += 1
print(s)
print(p)
