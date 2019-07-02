LIMIT = 10**6
ar = [0 for i in range(LIMIT)]
for d in range(1, LIMIT//4+1):
    const = 3*d*d
    mn = 2*d
    for z in range(1, d+1):
        n = const + z*mn - z*z
        if n >= LIMIT:
            break
        ar[n] += 1
    for z in range(3*d-1, d, -1):
        n = const + z*mn - z*z
        if n >= LIMIT:
            break
        ar[n] += 1
s = 0
for i in range(LIMIT):
    if ar[i] == 10:
        s += 1
print(s)
        
