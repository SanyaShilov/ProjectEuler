from primes import *
primelist = prime_list(20000000)
a = 3
b = 10
'''
r = range(a)
l1 = [i for i in range(1, a+1)]
l2 = [i for i in range(b-a+1, b+1)]
r1 = [0 for i in r]
r2 = [0 for i in r]
print('created')
for i in r :
    for j in primelist :
        if l1[i] < j :
            break
        while True :
            if l1[i] % j == 0 :
                r1[i] += j
                l1[i] /= j
            else :
                break
print('first')
for i in r :
    for j in primelist :
        if l2[i] < j :
            break
        while True :
            if l2[i] % j == 0 :
                r2[i] += j
                l2[i] /= j
            else :
                break
print('second')
res = 0
for n in r1 :
    res -= n

for n in r2 :
    res += n

print(res)
'''
g1 = 1
g2 = 5000000
g3 = 15000001
g4 = 20000000
g = 15000000
res = 0
for pr in primelist :
    temp = pr
    while temp <= g4 :
        res += pr * (g4//temp - g//temp - g2//temp)
        temp *= pr
print(res)
