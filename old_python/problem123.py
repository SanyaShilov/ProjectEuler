import euler

prime_list = euler.prime_list(1000000)

LIMIT = 10**10
n = 7037
p = prime_list[7037-1]
while True:
    n += 2
    p = prime_list[n-1]
    r = 2*p*n % (p*p)
    if r > LIMIT:
        print(n)
        break
    
