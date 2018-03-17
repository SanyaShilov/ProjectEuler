ar = [[], [{1}]]
limit = 200
for i in range(2, limit+1) :
    ar.append([])
    for j in range(i//2, i) :
        d = i - j
        for st in ar[j] :
            if d in st :
                ar[-1].append(st.union({i}))
    m = 10**10
    for st in ar[-1] :
        if len(st) < m :
            m = len(st)
    for st in ar[-1][:] :
        if len(st) > m :
            ar[-1].remove(st)

s = 0
for i in range(1, limit+1) :
    s += len(ar[i][0])-1 # -1 because we don't compute the n**1
print(s)
