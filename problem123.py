import euler

primelist = euler.primelist(1000000)

limit = 10**10
n = 7037
p = primelist[7037-1]
while True :
    n += 2
    p = primelist[n-1]
    r = 2*p*n % (p*p)
    if r > limit :
        print(n)
        break
    
