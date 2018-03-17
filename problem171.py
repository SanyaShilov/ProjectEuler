'''
l = 2000
little = [i*i for i in range(10)]
ar = [0 for i in range(l)]
for k in little :
    ar[k] = 1
ar[0] = 0
s = 0
for i in range(44) :
    s += ar[i*i]
print(s)
for _ in range(20-1) :
    newar = [0 for i in range(l)]
    for i in range(l) :
        if ar[i] :
            for q in little :
                newar[i+q] += ar[i]
    
    ar = newar
    for i in range(44) :
        s += ar[i*i]
print(s)
'''

fact = [1]
for i in range(1, 21) :
    fact.append(i*fact[-1])

repunits = [0]
for i in range(1, 21) :
    repunits.append(repunits[-1]*10+1)

sqar = [False for i in range(45*45+1)]
for i in range(45+1) :
    sqar[i*i] = True
dgsq = [i*i for i in range(10)]

def check (ar) :
    res = 0
    for i in range(1, 10) :
        res += dgsq[i]*ar[i]
    return sqar[res]

def perestanovki (ar, l) :
    res = fact[l]
    for k in ar :
        res //= fact[k]
    return res

def summ (ar, l) :
    s = 0
    for i in range(1, 10) :
        s +=i*ar[i]
    res = s*perestanovki(ar, l)*repunits[l]//l
    return res

arar = []
for i in range(10) :
    arar.append([0 for j in range(10)])
    arar[-1][i] = 1
arlast = [i for i in range(10)]
arlen = [1 for i in range(10)]
s = 0
while arar :
    ar = arar.pop()
    last = arlast.pop()
    l = arlen.pop()
    if l == 20 :
        if check(ar) :
            s += summ(ar, 20)
    elif l < 20 :
        l1 = l+1
        for i in range(last, 10) :
            newar = ar[:]
            newar[i] += 1
            arar.append(newar)
            arlast.append(i)
            arlen.append(l1)
print(s)
