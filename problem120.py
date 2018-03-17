mm = 0
for a in range(3, 1001) :
    aa = a**2
    m = 0
    for n in range(3, 2001, 2) :
        num = 2*a*n
        r = num % aa
        if r > m :
            m = r
    mm += m
print(mm)
# 332944222 with 1001
# 333082500 with 2001 !!!
