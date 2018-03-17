limit = 2*10**9

sq7 = [i*i for i in range(1, int((limit/7)**0.5+1))]
sq3 = [i*i for i in range(1, int((limit/3)**0.5+1))]
sq2 = [i*i for i in range(1, int((limit/2)**0.5+1))]
sq1 = [i*i for i in range(1, int((limit/1)**0.5+1))]
print(len(sq7), len(sq3), len(sq2), len(sq1))
set7 = set()
for a in sq7 :
    a7 = 7*a
    rest = limit - a7
    i = 0
    b = sq1[0]
    try : 
        while b <= rest :
            set7.add(a7+b)
            i += 1
            b = sq1[i]
    except :
        pass
print(len(set7))
