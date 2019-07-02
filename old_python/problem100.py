sq2 = 2**0.5

for s1 in range(1, 10000000):
    s2 = int(s1/sq2)
    if s1*s1-2*s2*s2 == 1:
        if 2*s2*(s1+s2) > 10**12:
            print((s1+s2)*s1)
            break
    s2 = int(s1*sq2)
    if 2*s1*s1-s2*s2 == 1:
        if 2*s1*(s1+s2) > 10**12:
            print((s1+s2)*s2+1)
            break
