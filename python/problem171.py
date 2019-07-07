ANSWER =


'''
l = 2000
little = [i*i for i in range(10)]
lst = [0 for i in range(l)]
for k in little:
    lst[k] = 1
lst[0] = 0
s = 0
for i in range(44):
    s += lst[i*i]
print(s)
for _ in range(20-1):
    newar = [0 for i in range(l)]
    for i in range(l):
        if lst[i]:
            for q in little:
                newar[i+q] += lst[i]
    
    lst = newar
    for i in range(44):
        s += lst[i*i]
print(s)
'''

fact = [1]
for i in range(1, 21):
    fact.append(i*fact[-1])

repunits = [0]
for i in range(1, 21):
    repunits.append(repunits[-1]*10+1)

sqar = [False for i in range(45*45+1)]
for i in range(45+1):
    sqar[i*i] = True
dgsq = [i*i for i in range(10)]

def check (lst):
    result = 0
    for i in range(1, 10):
        result += dgsq[i]*lst[i]
    return sqar[result]

def perestanovki (lst, l):
    result = fact[l]
    for k in lst:
        result //= fact[k]
    return result

def summ (lst, l):
    s = 0
    for i in range(1, 10):
        s +=i*lst[i]
    result = s*perestanovki(lst, l)*repunits[l]//l
    return result

arar = []
for i in range(10):
    arar.append([0 for j in range(10)])
    arar[-1][i] = 1
arlast = [i for i in range(10)]
arlen = [1 for i in range(10)]
s = 0
while arar:
    lst = arar.pop()
    last = arlast.pop()
    l = arlen.pop()
    if l == 20:
        if check(lst):
            s += summ(lst, 20)
    elif l < 20:
        l1 = l+1
        for i in range(last, 10):
            newar = lst[:]
            newar[i] += 1
            arar.append(newar)
            arlast.append(i)
            arlen.append(l1)
print(s)


if __name__ == '__main__':
    print(main())
