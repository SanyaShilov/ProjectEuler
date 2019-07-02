ANSWER =


def product (ar):
    res = 1
    for a in ar:
        res *= a
    return res

ar = (2, 2)
ars = {ar}
LIMIT = 12000
d = {k: k * 2 for k in range(2, LIMIT + 1)}
while ars:
    newars = set()
    for ar in ars:
        p = product(ar)
        k = p - sum(ar) + len(ar)
        if k > LIMIT:
            continue
        if d[k] > p:
            d[k] = p
        newars.add((ar[0] + 1,) + ar[1:])
        for i in range(1, len(ar)):
            if ar[i - 1] > ar[i]:
                newars.add(ar[:i] + (ar[i] + 1,) + ar[i + 1:])
        newars.add(ar + (2,))
    ars = newars
s = set(d.values())
print(sum(s))


if __name__ == '__main__':
    print(main())
