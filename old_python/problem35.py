ar = [i for i in range(1000000)]
for i in range(2, 1000):
    for j in range(2, 1000000//i+1000):
        try:
            ar[i*j] = 0
        except:
            pass
ar[1] = 0


s = 0
def get_round (n):
    st = str(n)
    return [int(st[i:]+st[:i]) for i in range(len(st))]

for i in range(1000000):
    a = ar[i]
    if a:
        g = get_round(a)
        t = 1
        for b in g:
            if ar[b] == 0:
                t = 0
        if t == 1:
            s += 1

print(s)
