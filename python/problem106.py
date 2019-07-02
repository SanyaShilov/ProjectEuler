import itertools

def pairs (n):
    t = tuple(i for i in range(1, n + 1))
    s = set()
    for i in range(2, len(t) + 1):
        l = (i + 2) // 2
        for perm in itertools.combinations(t, i):
            for i in range(1, l):
                for comb in itertools.combinations(perm, i):
                    second = tuple(a for a in perm if a not in comb)
                    if comb > second:
                        comb, second = second, comb
                    s.add((comb, second))
    return s

def check (pair):
    p1, p2 = pair
    l = len(p1)
    if l != len(p2):
        return False
    for i in range(l):
        if p1[i] > p2[i]:
            return True
    return False

p = pairs(12)
s = 0
for pair in p:
    s += check(pair)
print(s)


if __name__ == '__main__':
    print(main())
