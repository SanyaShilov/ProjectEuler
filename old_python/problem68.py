import itertools

lst = [6, 9, 8, 7, 10]

def calc (lst):
    result = [0, 0, 0, 0, 0]
    result[2] = lst[0]-lst[1]
    result[3] = lst[4]-lst[3]
    result[1] = result[3]+lst[2]-lst[1]
    result[4] = result[1]+lst[0]-lst[4]
    if len(set(result)) < 5:
        return None
    if max(result)-min(result) != 4:
        return None
    return result, 5-max(result)

m = 0
for a in itertools.permutations(lst, 5):
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
