import itertools


ANSWER =


ar = [6, 9, 8, 7, 10]

def calc (ar):
    res = [0, 0, 0, 0, 0]
    res[2] = ar[0]-ar[1]
    res[3] = ar[4]-ar[3]
    res[1] = res[3]+ar[2]-ar[1]
    res[4] = res[1]+ar[0]-ar[4]
    if len(set(res)) < 5:
        return None
    if max(res)-min(res) != 4:
        return None
    return res, 5-max(res)

m = 0
for a in itertools.permutations(ar, 5):
    if a[0] == 6:
        c = calc(a)
        if c:
            b = [k+c[1] for k in c[0]]
            r = ''
            for i in range(5):
                r += str(a[i])
                r += str(b[i])
                r += str(b[(i+1)%5])
            t = int(r)
            if t > m:
                m = t
print(m)


if __name__ == '__main__':
    print(main())
