s = 0
for i in range (2, 300000):
    lst = [int(d) for d in str(i)]
    if i == sum(k**5 for k in lst):
        s += i
print(s)
