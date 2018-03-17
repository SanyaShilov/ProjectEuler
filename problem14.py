tab = [0,
       1,
       2]

for i in range(3, 1000000) :
    temp = i
    l = 0
    while temp >= i :
        if temp % 2 :
            temp = temp*3 + 1
        else :
            temp //= 2
        l += 1
    tab.append(l+tab[temp])
print(tab.index(max(tab)))
