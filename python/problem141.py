ANSWER =


LIMIT = 10**12
sLIMIT = int(LIMIT**0.5)
sq = {i*i for i in range(1, sLIMIT+1)}

st = set()
for n in range(2,  int(LIMIT**(1/3))+1):
    n3 = n*n*n
    for a in range(1, LIMIT):
        if a*(a*n3+1) > LIMIT:
            break
        for m in range(1, n):
            q = a*m*(a*n3+m)
            if q > LIMIT:
                break
            if q in sq:
                st.add(q)
print(sum(st))


if __name__ == '__main__':
    print(main())
