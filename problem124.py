import euler

primelist = euler.primelist(100001)

lst = [[1, n] for n in range(100001)]

for pr in primelist :
    for i in range(pr, 100001, pr) :
        lst[i][0] *= pr

def sortkey (elem) :
    return elem[0]*1000000 + elem[1]

lst.sort(key = sortkey)

print(lst[10000][1])
