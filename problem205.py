a = [[1], [2], [3], [4]]
for i in range(8) :
    a = [k+[i] for k in a for i in range(1, 5)]
la = len(a)
ar = [0 for i in range(40)]
for i in range(la) :
    ar[sum(a[i])] += 1
print(ar)
b = [[1], [2], [3], [4], [5], [6]]
for i in range(5) :
    b = [k+[i] for k in b for i in range(1, 7)]
lb = len(b)
br = [0 for i in range(40)]
for i in range(lb) :
    br[sum(b[i])] += 1
print(br)
s = 0
for i in range(40) :
    ss = sum(br[:i])*ar[i]
    print(ss)
    s += ss
print(s)
print(s / (sum(ar)*sum(br)))
