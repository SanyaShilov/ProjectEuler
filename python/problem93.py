ANSWER =


def two_combination (a, b):
    if a != 0:
        if b != 0:
            return {a+b, a-b, a*b, a/b, b-a, b/a}
        return {a, -a, 0}
    return {b, -b, 0}

def three_combination (a, b, c):
    ab = two_combination(a, b)
    ac = two_combination(a, c)
    bc = two_combination(b, c)
    three = set()
    for n in ab:
        three.update(two_combination(n, c))
    for n in ac:
        three.update(two_combination(n, b))
    for n in bc:
        three.update(two_combination(n, a))
    return three

def four_combination (a, b, c, d):
    four = set()
    ab = two_combination(a, b)
    ac = two_combination(a, c)
    bc = two_combination(b, c)
    db = two_combination(d, b)
    dc = two_combination(d, c)
    da = two_combination(d, a)
    abc = three_combination(a, b, c)
    abd = three_combination(a, b, d)
    acd = three_combination(a, c, d)
    bcd = three_combination(b, c, d)
    for n in ab:
        for m in dc:
            four.update(two_combination(n, m))
    for n in ac:
        for m in db:
            four.update(two_combination(n, m))
    for n in da:
        for m in bc:
            four.update(two_combination(n, m))
    for n in abc:
        four.update(two_combination(n, d))
    for n in abd:
        four.update(two_combination(n, c))
    for n in acd:
        four.update(two_combination(n, b))
    for n in bcd:
        four.update(two_combination(n, a))
    return four

def clean (st):
    return set(round(i) for i in st if i >= 0 and abs(i-round(i)) < 1e-3)

def result (a, b, c, d):
    return clean(four_combination(a, b, c, d))

def length (result):
    i = 1
    while i in result:
        i += 1
    return i-1

n = 0
m = 0
for i in range(3, 10):
    for j in range(i+1, 10):
        l = length(result(1, 2, i, j))
        if l > m:
            n = 1200+10*i+j
            m = l
print(n)


if __name__ == '__main__':
    print(main())
