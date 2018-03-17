import euler

primelist = euler.primelist(10000)

def add (ar, num) :
    newar = []
    j = primelist.index(num)
    for i in ar[:] :
        c = i[:]
        c[j] += 1
        newar.append(c)
    return newar

def sumtwo (n, ind) :
    result = []
    i = ind
    pr = primelist[i]
    n2 = n//2
    while pr <= n2 :
        j = i
        rest = n - pr
        pr2 = primelist[j]
        while pr2 <= rest :
            if pr2 == rest :
                result.append([0 for p in range(j+1)])
                result[-1][i] += 1
                result[-1][j] += 1
            j += 1
            pr2 = primelist[j]
        i += 1
        pr = primelist[i]
    return result
    
def sumcount (n, count, ind = 0) :
    if n < count * 2 :
        return []
    if count == 2 :
        return sumtwo(n, ind)
    i = ind
    pr = primelist[i]
    smallest = n//count
    res = []
    while pr <= smallest :
        res += add(sumcount(n-pr, count-1, i), pr)
        i += 1
        pr = primelist[i]
    return res

def sumall (n) :
    c = 2
    temp = sumcount(n, c)
    res = []
    while n > 2*c :
        res += temp
        c += 1
        temp = sumcount(n, c)
    return res

i = 1
while True :
    i += 1
    r = sumall(i)
    l = len(r)
    if l > 5000 :
        print(i)
        break