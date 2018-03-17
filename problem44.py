def penta (n) :
    return n*(3*n-1)//2

def is_penta (n) :
    a = (1+(1+24*n)**0.5)/6
    return round(a) == round(a, 7)

mas = [penta(i) for i in range(1, 100000)]


mind = 0
for i in range(100000-1) :
    for j in range(i) :
        mi = mas[i]
        mj = mas[j]
        if is_penta(mi-mj) :
            if is_penta(mi+mj) :
                d = mi-mj
                if mind == 0 or mind > d :
                    mind = d
                    print(mind)
                    exit()
