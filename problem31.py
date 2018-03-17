coins = [1, 2, 5, 10, 20, 50, 100, 200]
sums = [0]
arind = [0]
s = 0
while sums :
    sm = sums.pop()
    ind = arind.pop()
    if sm == 200 :
        s += 1
    else :
        for i in range(ind, 8) :
            ss = sm + coins[i]
            if ss > 200 :
                break
            sums.append(ss)
            arind.append(i)
print(s)
