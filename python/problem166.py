ANSWER =


def sum_row (lst, i):
    return sum(lst[i])

def sum_column (lst, i):
    return sum(a[i] for a in lst)

def sum_diag_main (lst):
    return sum(a[i] for i, a in enumerate(lst))

def sum_diag_sub (lst):
    return sum(a[3 - i] for i, a in enumerate(lst))

def convert_to_int (lst):
    n = 0
    for i in range(4):
        for j in range(4):
            n <<= 4
            n += lst[i][j]
    return n

def check (n):
    while n:
        if n & 15 > 9:
            return False
        n >>= 4
    return True

def convert_to_ar (n):
    lst = [[0 for i in range(4)] for j in range(4)]
    for i in range(3, -1, -1):
        for j in range(3, -1, -1):
            lst[i][j] = n & 15
            n >>= 4
    return lst

lst = [[0 for i in range(4)] for j in range(4)]
ones = {s: set() for s in range(0, 4 + 1)}
for n in range(2**16):
    for i in range(4):
        for j in range(4):
            lst[i][j] = n & 1
            n >>= 1
    s = sum_row(lst, 0)
    if (sum_row(lst, 1) == s and
        sum_row(lst, 2) == s and
        sum_row(lst, 3) == s and
        sum_column(lst, 0) == s and
        sum_column(lst, 1) == s and
        sum_column(lst, 2) == s and
        sum_column(lst, 3) == s and
        sum_diag_main(lst) == s and
        sum_diag_sub(lst) == s):
        ones[s].add(convert_to_int(lst))
ones.pop(0)
d = {s: set() for s in range(0, 36 + 1)}
d[0].add(0)
for i in range(1, 36 + 1):
    print(i, len(d[i - 1]))
    for j in range(max(0, i - 4), i):
        diff = i - j
        for ds in d[j]:
            for one in ones[diff]:
                new = ds + one
                if check(new):
                    d[i].add(new)
count = 0
for s in d.values():
    count += len(s)
print(count)

# 5732642 is wrong


if __name__ == '__main__':
    print(main())
