import euler

def gcd1 (a, b):
    ''' a < b '''
    if a == 1:
        return True
    if not a:
        return False
    return gcd1(b%a, a)

LIMIT = 120000
prime_list = euler.prime_list(LIMIT + 1000)

rads = [1 for i in range(LIMIT)]
for pr in prime_list:
    for i in range(pr, LIMIT, pr):
        rads[i] *= pr

squares = [i*i for i in range(2, int(LIMIT**0.5) + 1)]
square_divisibles = sorted({sq * i for sq in squares for i in range(1, LIMIT//sq + 1)})

count = 0
for ic in range(len(square_divisibles)):
    c = square_divisibles[ic]
    if c >= LIMIT:
        break
    if c % 1000 == 0:
        print(c)
    c_2 = c//2
    d = c / rads[c]
    for ib in range(ic - 1, -1, -1):
        b = square_divisibles[ib]
        if b <= c_2:
            break
        if rads[c - b]*rads[b] < d:
            if gcd1(b, c):
                #print(c - b, b, c)
                count += c
print(count)

# 18407904, 10 minutes
