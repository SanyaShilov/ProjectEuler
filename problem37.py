ar = [i for i in range(1000000)]
for i in range(2, 1000) :
    for j in range(2, 1000000//i+1000) :
        try :
            ar[i*j] = 0
        except :
            pass
s = 0
ar[1] = 0
for i in range(10, 1000000) :
    if ar[i] != 0 :
        tr = 1
        ind = i
        l = len(str(i))
        for j in range(l-1) :
            ind = ind // 10
            if ar[ind] == 0 :
                tr = 0
                break
        if tr == 1 :
            ind = i
            for j in range(l-1) :
                ind = ind % 10**(l-1-j)
                if ar[ind] == 0 :
                    tr = 0
                    break
        if tr == 1 :
            s += i
print(s)
