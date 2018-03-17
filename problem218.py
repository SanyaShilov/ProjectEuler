#
def gcd1 (a, b) :
    if a == 1 :
        return True
    if not a :
        return False
    if a > b :
        return gcd1(a%b, b)
    return gcd1(b%a, a)

for a in range(2, 1000) :
    a2 = a*a
    for b in range(1, a) :
        if gcd1(b, a) :
            b2 = b*b
            a2b2m = a2-b2
            ab = 2*a*b
            a2b2p = a2+b2
            if gcd1(a2b2m, ab) :
                if a2b2m > ab :
                    biga = a2b2m
                    bigb = ab
                else :
                    biga = ab
                    bigb = a2b2m
                sa = biga*biga-bigb*bigb
                sb = 2*biga*bigb
                sc = a2b2p*a2b2p
                area = sa*sb//2
                if area % 6 :
                    print(sa, sb, sc)
                elif area % 28 :
                    print(sa, sb, sc)
