limit = 10**12
slimit = int(limit**0.5)
sq = {i*i for i in range(1, slimit+1)}

st = set()
for n in range(2,  int(limit**(1/3))+1) :
    n3 = n*n*n
    for a in range(1, limit) :
        if a*(a*n3+1) > limit :
            break
        for m in range(1, n) :
            q = a*m*(a*n3+m)
            if q > limit :
                break
            if q in sq :
                st.add(q)
print(sum(st))
