import itertools

def check (ar):
    prev_max = ar[0]
    for i in range(2, len(ar)):
        s = set()
        for comb in itertools.combinations(ar, i):
            sm = sum(comb)
            if sm <= prev_max:
                return False
            if sm in s:
                return False
            s.add(sm)
        prev_max = max(s)
    return True

def build (n):
    if n < 5:
        ar = tuple(i for i in reversed(range(1, n + 1)))
    else:
        b = build(n - 1)
        ar = (b[0] + 1,) + b
        ar = tuple(a + b[-1]//2 for a in ar)
        print('started from', ar)
    ars = {ar}
    it = 0
    while True:
        if n == 7:
            print(it, len(ars))
            it += 1
        newars = set()
        for ar in ars:
            if check(ar):
                print('return', ar)
                return ar
            add = True
            if n > 5:
                for i in range(1, n):
                    if ar[i - 1] - ar[i] >= ar[-1]:
                        add = False
                        break
            if add:
                newars.add((ar[0] + 1,) + ar[1:])
                for i in range(1, n):
                    if ar[i - 1] - ar[i] > 1:
                        newars.add(ar[:i] + (ar[i] + 1,) + ar[i + 1:])
        ars = newars

print(build(7))
