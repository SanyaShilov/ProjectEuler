# x = n + i, y = n + j

import euler

prime_list = euler.prime_list(100)
result = 10**1000
LIMIT = 10**3

def decisions (lst):
    result = 1
    for a in lst:
        if a == 0:
            break
        result *= (a << 1) + 1
    return result // 2 + 1

def number (lst):
    result = 1
    for i in range(len(lst)):
        if lst[i] == 0:
            break
        result *= prime_list[i]**lst[i]
    return result

def new_arrays (lst):
    yield (lst[0] + 1,) + lst[1:]
    for i in range(1, len(lst)):
        if lst[i - 1] == 0:
            return
        if lst[i] < lst[i - 1]:
            yield lst[:i] + (lst[i] + 1,) + lst[i + 1:]

lst = tuple(0 for i in range(len(prime_list)))
ars = {lst}
while ars:
    newars = set()
    for lst in ars:
        n = number(lst)
        if n > result:
            continue
        if decisions(lst) > LIMIT:
            result = n
        for newar in new_arrays(lst):
            newars.add(newar)
    ars = newars
print(result)


if __name__ == '__main__':
    print(main())
