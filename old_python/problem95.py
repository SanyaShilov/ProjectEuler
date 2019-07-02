import array

def sumdivisors (n):
    i = (1 for i in range(n+1))
    res = array.array('L', i)
    for i in range(2, n//2):
        for j in range(2, n//i+1):
            res[i*j] += i
    return res

ar = sumdivisors(1000000)
mxl = 0
value = 0

def length (start):
    global mxl
    global value
    l = 1
    ind = ar[start]
    while ind > start:
        if l > 100:
            return
        if ind >= 1000000:
            return
        ind = ar[ind]
        l += 1
    if ind == start:
        if l > mxl:
            mxl = l
            value = start

for i in range(1, 1000000):
    length(i)

print(value)
