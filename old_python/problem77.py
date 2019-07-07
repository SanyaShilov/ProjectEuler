import euler

prime_list = euler.prime_list(10000)

def add (lst, num):
    newar = []
    j = prime_list.index(num)
    for i in lst[:]:
        c = i[:]
        c[j] += 1
        newar.append(c)
    return newar

def sumtwo (n, ind):
    result = []
    i = ind
    pr = prime_list[i]
    n2 = n//2
    while pr <= n2:
        j = i
        rest = n - pr
        pr2 = prime_list[j]
        while pr2 <= rest:
            if pr2 == rest:
                result.append([0 for p in range(j+1)])
                result[-1][i] += 1
                result[-1][j] += 1
            j += 1
            pr2 = prime_list[j]
        i += 1
        pr = prime_list[i]
    return result
    
def sumcount (n, count, ind = 0):
    if n < count * 2:
        return []
    if count == 2:
        return sumtwo(n, ind)
    i = ind
    pr = prime_list[i]
    smallest = n//count
    result = []
    while pr <= smallest:
        result += add(sumcount(n-pr, count-1, i), pr)
        i += 1
        pr = prime_list[i]
    return result

def sumall (n):
    c = 2
    temp = sumcount(n, c)
    result = []
    while n > 2*c:
        result += temp
        c += 1
        temp = sumcount(n, c)
    return result

i = 1
while True:
    i += 1
    r = sumall(i)
    l = len(r)
    if l > 5000:
        print(i)
        break
