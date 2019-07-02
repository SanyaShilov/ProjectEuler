ANSWER =


def gcd1 (a, b):
    if a == 1:
        return True
    if not a:
        return False
    if a > b:
        return gcd1(a%b, b)
    return gcd1(b%a, a)

s = 0
LIMIT = 1000000*100

for a in range(2, int(LIMIT**0.25)):
    a2 = a*a
    for b in range(1, a):
        b2 = b*b
        a2b2m = a2-b2
        ab = 2*a*b
        a2b2p = a2+b2
        per = a2b2m+ab+a2b2p
        if per >= LIMIT:
            break
        if gcd1(a2b2m, ab):
            if a2b2m > ab:
                dif = a2b2m - ab
            else:
                dif = ab - a2b2m
            if not a2b2p % dif:
                s += (LIMIT-1)//per

s = 0
a, b = 2, 1
while True:
    per = 2*a*(a+b)
    if per > LIMIT:
        break
    s += (LIMIT-1)//per
    a, b = 2*a+b, a
print(s)


if __name__ == '__main__':
    print(main())
