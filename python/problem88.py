ANSWER =


def product (lst):
    result = 1
    for a in lst:
        result *= a
    return result

lst = (2, 2)
ars = {lst}
LIMIT = 12000
d = {k: k * 2 for k in range(2, LIMIT + 1)}
while ars:
    newars = set()
    for lst in ars:
        p = product(lst)
        k = p - sum(lst) + len(lst)
        if k > LIMIT:
            continue
        if d[k] > p:
            d[k] = p
        newars.add((lst[0] + 1,) + lst[1:])
        for i in range(1, len(lst)):
            if lst[i - 1] > lst[i]:
                newars.add(lst[:i] + (lst[i] + 1,) + lst[i + 1:])
        newars.add(lst + (2,))
    ars = newars
s = set(d.values())
print(sum(s))


if __name__ == '__main__':
    print(main())
