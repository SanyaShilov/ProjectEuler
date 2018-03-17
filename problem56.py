def dsum (n) :
    return sum(int(k) for k in str(n))

m = 0
for i in range(1, 100) :
    for j in range(1, 100) :
        d = dsum(i**j)
        if d > m :
            m = d
print(m)
