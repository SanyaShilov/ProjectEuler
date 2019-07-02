# C

import array

def prime_list (n):
    index = array.array('L', (1 for i in range(n)))
    
    i = 2
    while i < n:
        if index[i]:
            j = i+i
            while j < n:
                index[j] = 0
                j += i
        i += 1
    index[0] = index[1] = 0
    return index

def max_deLIMITer (n):
    i = 0
    pr = prime_list[0]
    sq = (n+1)**0.5
    while pr < sq:
        if n % pr == 0:
            n //= pr
            sq = (n+1)**0.5
            i -= 1
        i += 1
        pr = prime_list[i]
    return n

s = 0


LIMIT = 10000000
LIMIT1= LIMIT+1
powerlist = prime_list(LIMIT+1)
fastlist = prime_list(LIMIT+1)
prime_list = []

for i in range(len(powerlist)):
    if powerlist[i]:
        prime_list.append(i)
        
for i in range(len(powerlist)-1, -1, -1):
    if powerlist[i]:
        temp = i
        while temp < LIMIT1:
            powerlist[temp]= 1
            temp *= i
            
for n in range(2, LIMIT+1):
    if powerlist[n]:
        s += 1
        continue
    
    if not n&1:
        if fastlist[n//2]:
            s += n//2+1
            continue
        
    m = max_deLIMITer(n)
    r = n//m
    for a in range(r-1, 0, -1):
        am = a*m
        if not am*(am+1)%n:
            s += am+1
            break
        if not am*(am-1)%n:
            s += am
            break
        
print(s)
