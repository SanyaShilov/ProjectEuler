s = 0
for i in range (2, 1000000) :
    ar = [int(d) for d in str(i)]
    if i == sum(k**5 for k in ar) :
        s += i
print(s)
