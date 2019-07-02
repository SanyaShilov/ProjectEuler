LIMIT = 10**6

def shortest_path (a, b, c):
    return ((a + b)**2 + c**2)**0.5

def gcd1 (a, b):
    ''' a <= b '''
    if a == 1:
        return True
    if not a:
        return False
    return gcd1(b%a, a)

def pythagorean_unique_trio (a):
    a2 = a*a
    for b in range(1, a):
        b2 = b*b
        x = a2-b2
        y = 2*a*b
        if gcd1(x, y):
            yield x, y
            yield y, x

def count_of_c (c, a_b):
    if a_b > c:
        if c < (a_b >> 1):
            return 0
        return c - ((a_b - 1) >> 1)
    else:
        return a_b >> 1
        

l = []
for a in range(1, 1000):
    for pair in pythagorean_unique_trio(a):
        l.append(pair)
l.sort()
#for pair in l:
#    print(pair)
print(l[-1], len(l))
'''
count = 0
for a in range(1, LIMIT + 1):
    for b in range(a, LIMIT + 1):
        for c in range(b, LIMIT + 1):
            s = shortest_path(a, b, c)
            if round(s, 13).is_integer():
                count += 1
print(count)
'''
'''
count = 0
for c in range(1, LIMIT + 1):
    for a in range(1, c + 1):
        for b in range(a, c + 1):
            s = shortest_path(a, b, c)
            if round(s, 13).is_integer():
                count += 1
    #print(c, count)
print(count)
'''
count = 0
for c in range(1, LIMIT + 1):
    for pair in l:
        if pair[0] > c:
            break
        if c % pair[0] == 0:
            d = c // pair[0]
            count += count_of_c(c, pair[1]*d)
    if count > LIMIT:
        print(c, count)
        break
