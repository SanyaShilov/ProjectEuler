import array

l = 250

#more than 30000
'''
ar = [[0 for i in range(l)] for j in range(l)]
ar[0][0] = 1
for i in range(1, l) :
    res = 0
    for j in range(i) :
        temp = 0
        for k in range(j+1) :
            temp += ar[i-j-1][k]
        ar[i][j] = temp
        res += temp
    print(i)
    if res % 1000000 == 0 :
        print(i)
        break
'''


ar = [[0 for i in range(l)] for j in range(l)]
ar[0][0] = 1
for i in range(1, l) :
    for j in range(i) :
        ar[i][j] = sum(ar[i-j-1][:j+1])
print(sum(ar[234]))


l = 60000

r = range(l+1)

summed = [array.array('L', (1,)) for i in r]

def gsum (i, j) :
    global ar, summed
    ind = i-j-1
    if j >= ind :
        return summed[ind][-1]
    if j == 0 :
        return 1
    temp = (summed[ind][j-1]+ar[ind][j])%1000000
    summed[ind].append(temp)
    return temp


ar = [array.array('L') for i in r]
print('done')
ar[0].append(1)
i = 1
for i in range(1, l+1) :
    res = 0
    for j in range(i) :
        temp = gsum(i, j)
        res += temp
        ar[i].append(temp)
    if not res % 1000000 :
        print(i)
        break
    if not i % 1000 :
        print(i)

'''
for k in summed :
    print(k)
for k in ar :
    print(k)

'''



