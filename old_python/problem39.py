# (a+n)**2 + (b+n)**2 = (a+b+n)** 2 -> n**2 = 2*a*b
ar = [0 for k in range(1001)]
for n in range(1, 400):
    for a in range(1, 500):
        if n**2 % (2*a) == 0:
            b = n**2//(2*a)
            p = 2*a + 2*b + 3*n
            if p <= 1000:
                ar[p] += 1
print(ar.index(max(ar)))
