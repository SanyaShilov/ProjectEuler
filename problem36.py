s = 0
for i in range(1, 1000000) :
    if i == int(str(i)[::-1]) :
        b = bin(i)[2:]
        if b == b[::-1] :
            s += i
print(s)
