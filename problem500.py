import euler
primelist = euler.primelist(7376513) # 500500 primes
l = len(primelist)
ar = [1 for i in range(l)]
pb = 0
pe = l-1
while ar[pb] :
    pw1 = ar[pb]+1
    if primelist[pb]**pw1 < primelist[pe] :
        ar[pe] = 0
        ar[pb] += pw1
        pe -= 1
    else :
        pb += 1
n = 1
for i in range(l) :
    n = (n*primelist[i]**ar[i])%500500507
print(n)
