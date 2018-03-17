def all_divizors (n) :
    d = 0
    for i in range(1, n+1) :
        if n % i == 0 :
            d += 1
    return d

d1 = all_divizors(1)
d2 = all_divizors(3)
i = 4
num = 3
    
while True :
    num = int(i*(i-1)/2)
    
    d1 = d2
    d2 = all_divizors(i)
    i += 1
    if d1 * d2 > 500 :
        if all_divizors(num) > 500 :
            print(num)
            break
