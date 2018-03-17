def f (n) :
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

table = [[n, f(n), 1] for n in range(1, 12)]

def square_approximation (x, y, n, w = None) :
    if not w :
        w = [1 for i in range(len(x))]
    matrix = [[0 for j in range(n+1)] for i in range(n)]
    for i in range(n) :
        for j in range(n) :
            sumA, sumB = 0, 0
            for k in range(len(x)) :
                sumA += x[k]**i * x[k]**j * w[k]
            matrix[i][j] = sumA
        for k in range(len(x)) :
            sumB += y[k] * x[k]**i * w[k]
        matrix[i][n] = sumB
    return matrix

def swapstr (a, i, j) :
    a[i], a[j] = a[j][:], a[i][:]

def Gauss (a) :
    l = len(a)
    r = range(len(a))
    swp = 0
    ind = [i for i in r]
    for i in r :
        for j in range(i+1, l) :
            if a[i][i] == 0 :
                swapstr(a, i, j)
                ind[i], ind[j] = ind[j], ind[i]
                swp += 1
        if a[i][i] == 0 :
            return 0
        else :
            for j in range(i+1, l) :
                q = a[j][i]/a[i][i]
                for k in range(l+1) :
                    a[j][k] = a[j][k]-a[i][k]*q
                    
    for i in range(l-1, 0, -1) :
        for j in range(i) :
            q = a[j][i]/a[i][i]
            for k in range(l+1) :
                a[j][k] = a[j][k]-a[i][k]*q

    C = [0 for k in r]
    for i in r :
        C[ind[i]] = round(a[i][-1]/a[i][i])
    return C



s = 0
for n in range(1, 11) :
    newtable = table[:n]

    r = range(len(newtable))

    x = [table[i][0] for i in r]
    y = [table[i][1] for i in r]
    w = [table[i][2] for i in r]
    
    matrix = square_approximation(x, y, n, w)

    C = Gauss(matrix)

    ymyfi = []
    
    X = [min(x)+k*(max(x)-min(x))/100 for k in range(101)]
    for i in range(1, int(X[-1]+1)) :
        fi = f(i)
        myfi = sum(C[j]*i**j for j in range(n))
        ymyfi.append(myfi)

    
    need = True
    while need :
        need = False
        for i in r :
            if y[i] != ymyfi[i] :
                need = True
        if need :
            diff = []
            for i in r :
                diff.append(y[i]-ymyfi[i])
            m = square_approximation(x, diff, n, w)
            C2 = Gauss(m)
            for i in r :
                C[i] += C2[i]

        ymyfi = []
        for i in range(1, int(X[-1]+1)) :
            fi = f(i)
            myfi = sum(C[j]*i**j for j in range(n))
            ymyfi.append(myfi)

    s += sum(C[j]*(int(X[-1]+1))**j for j in range(n))
    
print(s)
