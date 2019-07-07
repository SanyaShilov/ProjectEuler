a = [[1], [2], [3], [4]]
for i in range(8):
    a = [k+[i] for k in a for i in range(1, 5)]
la = len(a)
lst = [0 for i in range(40)]
for i in range(la):
    lst[sum(a[i])] += 1
print(lst)
b = [[1], [2], [3], [4], [5], [6]]
for i in range(5):
    b = [k+[i] for k in b for i in range(1, 7)]
lb = len(b)
br = [0 for i in range(40)]
for i in range(lb):
    br[sum(b[i])] += 1
print(br)
s = 0
for i in range(40):
    ss = sum(br[:i])*lst[i]
    print(ss)
    s += ss
print(s)
print(s / (sum(lst)*sum(br)))
