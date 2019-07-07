import euler
import itertools

LIMIT = 10**16

prime_list = euler.prime_list(100)

def product (lst):
    a = 1
    for i in lst:
        a *= i
    return a
'''
s = set()
l = 0
for c in itertools.combinations(prime_list, 4):
    l += 1
    a = product(c)
    for i in range(a, LIMIT, a):
        s.add(i)
print(len(s))
'''

s = 0
l = 0
for c in itertools.combinations(prime_list, 4):
    l += 1
    if not l % 100:
        print(l)
    lst = []
    m = c[-1]
    for pr in prime_list:
        if pr < m and pr not in c:
            lst.append(pr)
    a = 1
    for pr in c:
        a *= pr
    s += euler.notdivisible(LIMIT//a, lst, len(lst))
print(s)


if __name__ == '__main__':
    print(main())
