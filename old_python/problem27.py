lst = [i for i in range(1000)]
for i in range(2, 32):
    for j in range(2, 1000//i+32):
        try:
            lst[i*j] = 0
        except:
            pass

ml = 0
ma = 0
mb = 0
for b in lst:
    if b > 2:
        for a in range(-999, 1001, 2):
            n = 0
            l = 0
            c = b
            while lst[c] != 0:
                n += 1
                l += 1
                c = n**2+a*n+b
                if c < 0 or c > 999:
                    break
            if l > ml:
                ml = l
                ma = a
                mb = b
print(ma*mb)
