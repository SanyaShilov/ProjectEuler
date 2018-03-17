tr = [i * (i+1) // 2 for i in range(1, 1000000)]
pn = [i * (3*i-1) // 2 for i in range(1, 1000000)]
hx = [i * (2*i-1) for i in range(1, 1000000)]
t = 0
p = 2
h = 200
while tr[t] != pn[p] or tr[t] != hx[h] :
    t += 1
    if tr[t] > pn[p] :
        p += 1
    if tr[t] > hx[h] :
        h += 1
print(tr[t])
