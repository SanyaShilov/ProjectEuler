def pandigital (n) :
    ar = [False for k in range(10)]
    while n :
        r = n % 10
        if ar[r] :
            return False
        ar[r] = True
        n //= 10
    return True

def ipandigital (n, i) :
    ar = [False for k in range(10)]
    ar[i] = True
    while n :
        r = n % 10
        if ar[r] :
            return False
        ar[r] = True
        n //= 10
    return True

def jpandigital (n, j) :
    ar = [False for k in range(10)]
    while j :
        ar[j % 10] = True
        j //= 10
    while n :
        r = n % 10
        if ar[r] :
            return False
        ar[r] = True
        n //= 10
    return True

def ijpandigital (n, i, j) :
    ar = [False for k in range(10)]
    ar[i] = True
    while j :
        ar[j % 10] = True
        j //= 10
    while n :
        r = n % 10
        if ar[r] :
            return False
        ar[r] = True
        n //= 10
    return True

for i in range(2, 10) :
    print(i)
    for j in range(10000) :
        if ipandigital(j, i) :
            if pandigital(i*j) :
                if str(i*j)[:2] == '98' :
                    for k in range(400000, 450000) :
                        if len(str(i*j)+str(i*k)) == 10 :
                            if ijpandigital(k, i, j) :
                                if jpandigital(k*i, i*j) :
                                    print(i, j, k, i*j, i*k)
                    
