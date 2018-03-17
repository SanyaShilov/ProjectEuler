# C

import euler

limit = 1000000

primelist = euler.primelist(limit+1000)
s = 0
ten = 1
        
for i in range(2, len(primelist)) :
    pr1 = primelist[i]
    if pr1 > limit :
        break
    pr2 = primelist[i+1]
    rest = pr2 - pr1
    if ten < pr1 :
        ten *= 10
    start = ten
    while start % pr2 != rest :
        start += ten
    s += start + pr1
print(s)

