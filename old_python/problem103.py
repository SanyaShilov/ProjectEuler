import itertools

def check (lst):
    prev_max = lst[0]
    for i in range(2, len(lst)):
        s = set()
        for comb in itertools.combinations(lst, i):
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
        lst = tuple(i for i in reversed(range(1, n + 1)))
    else:
        b = build(n - 1)
        lst = (b[0] + 1,) + b
        lst = tuple(a + b[-1]//2 for a in lst)
        print('started from', lst)
    ars = {lst}
    it = 0
    while True:
        if n == 7:
            print(it, len(ars))
            it += 1
        newars = set()
        for lst in ars:
            if check(lst):
                print('return', lst)
                return lst
            add = True
            if n > 5:
                for i in range(1, n):
                    if lst[i - 1] - lst[i] >= lst[-1]:
                        add = False
                        break
            if add:
                newars.add((lst[0] + 1,) + lst[1:])
                for i in range(1, n):
                    if lst[i - 1] - lst[i] > 1:
                        newars.add(lst[:i] + (lst[i] + 1,) + lst[i + 1:])
        ars = newars

print(build(7))
