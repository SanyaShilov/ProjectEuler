# C

import array

def prime_list (n) :
    index = array.array('L', (1 for i in range(n)))
    
    i = 2
    while i < n :
        if index[i] :
            j = i+i
            while j < n :
                index[j] = 0
                j += i
        i += 1
    index[0] = index[1] = 0
    return index

def max_delimiter (n) :
    i = 0
    pr = primelist[0]
    sq = (n+1)**0.5
    while pr < sq :
        if n % pr == 0 :
            n //= pr
            sq = (n+1)**0.5
            i -= 1
        i += 1
        pr = primelist[i]
    return n

s = 0


limit = 10000000
limit1= limit+1
powerlist = prime_list(limit+1)
fastlist = prime_list(limit+1)
primelist = []

for i in range(len(powerlist)) :
    if powerlist[i] :
        primelist.append(i)
        
for i in range(len(powerlist)-1, -1, -1) :
    if powerlist[i] :
        temp = i
        while temp < limit1 :
            powerlist[temp]= 1
            temp *= i
            
for n in range(2, limit+1) :
    if powerlist[n] :
        s += 1
        continue
    
    if not n&1 :
        if fastlist[n//2] :
            s += n//2+1
            continue
        
    m = max_delimiter(n)
    r = n//m
    for a in range(r-1, 0, -1) :
        am = a*m
        if not am*(am+1)%n :
            s += am+1
            break
        if not am*(am-1)%n :
            s += am
            break
        
print(s)
