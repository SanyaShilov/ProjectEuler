n = 50000000
nn = int(n**0.5)+20
nnn = int(n**(1/3))+20
nnnn = int(nn**0.5)+20
arr = [i for i in range(nn)]
arr[1] = 0
for i in range(2, nnnn) :
    for j in range(2, nn//i+nnnn) :
        try :
            arr[i*j] = 0
        except :
            pass
arrr = arr[:nnn]
arrrr = arr[:nnnn]
s = set()
for i in arrrr :
    if i != 0 :
        for j in arrr :
            if j != 0 :
                temp = i**4 + j**3
                if temp < n :
                    for k in arr :
                        if k != 0 :
                            temp = i**4 + j**3 + k**2
                            if temp < n :
                                s.add(temp)
print(len(s))







































