import itertools


ANSWER = 20313839404245


def check(st):
    prev_max = st[0]
    for i in range(2, len(st)):
        combination_sums = set()
        for comb in itertools.combinations(st, i):
            combination_sum = sum(comb)
            if combination_sum <= prev_max:
                return False
            if combination_sum in combination_sums:
                return False
            combination_sums.add(combination_sum)
        prev_max = max(combination_sums)
    return True


def build(n):
    if n < 5:
        st = tuple(range(n, 0, -1))
    else:
        b = build(n - 1)
        st = (b[0] + 1,) + b
        st = tuple(a + b[-1] // 2 for a in st)
    ars = {st}
    while True:
        new_ars = set()
        for st in ars:
            if check(st):
                return st
            add = True
            if n > 5:
                for i in range(1, n):
                    if st[i - 1] - st[i] >= st[-1]:
                        add = False
                        break
            if add:
                new_ars.add((st[0] + 1,) + st[1:])
                for i in range(1, n):
                    if st[i - 1] - st[i] > 1:
                        new_ars.add(st[:i] + (st[i] + 1,) + st[i + 1:])
        ars = new_ars


def main():
    return int(''.join(str(n) for n in sorted(build(7))))


if __name__ == '__main__':
    print(main())
