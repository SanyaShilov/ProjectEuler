# x = n + i, y = n + j

import euler

prime_list = euler.prime_list(100)
result = 10**1000
LIMIT = 4 * 10**6

def decisions (ar):
    res = 1
    for a in ar:
        if a == 0:
            break
        res *= (a << 1) + 1
    return res // 2 + 1

def number (ar):
    res = 1
    for i in range(len(ar)):
        if ar[i] == 0:
            break
        res *= prime_list[i]**ar[i]
    return res

def new_arrays (ar):
    yield (ar[0] + 1,) + ar[1:]
    for i in range(1, len(ar)):
        if ar[i - 1] == 0:
            return
        if ar[i] < ar[i - 1]:
            yield ar[:i] + (ar[i] + 1,) + ar[i + 1:]

ar = tuple(0 for i in range(len(prime_list)))
ars = {ar}
while ars:
    newars = set()
    for ar in ars:
        n = number(ar)
        if n > result:
            continue
        if decisions(ar) > LIMIT:
            result = n
        for newar in new_arrays(ar):
            newars.add(newar)
    ars = newars
print(result)


if __name__ == '__main__':
    print(main())
