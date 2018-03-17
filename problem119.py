# 48
def sum_d (n) :
    s = 0
    st = str(n)
    l = len(st)
    for i in range(l) :
        s += ord(st[i])
    return s - l*48
n = 1
ar = []
for i in range (2, 2000) :
    for j in range(2, 100) :
        num = i**j
        if sum_d(num) == i :
            ar.append(num)
            n += 1
ar.sort()
print(ar[30-1])
