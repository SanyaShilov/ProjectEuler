import euler

d1 = euler.count_divisors(2)

d2 = euler.count_divisors(3)
i = 4
num = 3
    
while True:
    num = int(i*(i-1)/2)
    
    d1 = d2
    d2 = euler.count_divisors(i)
    i += 1
    if d1 * d2 > 500:
        if euler.count_divisors(num) > 500:
            print(num)
            break

