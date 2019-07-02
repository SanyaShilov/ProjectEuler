import array

l = 101

#more than 30000



arr = [[0 for i in range(l)] for j in range(l)]
arr[0][0] = 1
for i in range(1, l):
    for j in range(i):
        arr[i][j] = sum(arr[i-j-1][:j+1])

l = 101

r = range(l+1)

summed = [array.array('L', (1,)) for i in r]

def gsum (i, j):
    global ar, summed
    ind = i-j-1
    if j >= ind:
        return summed[ind][-1]
    if j == 0:
        return 1
    temp = (summed[ind][j-1]+ar[ind][j])%1000000
    summed[ind].append(temp)
    return temp


ar = [array.array('L') for i in r]
print('done')
ar[0].append(1)
i = 1
for i in range(1, l+1):
    res = 0
    for j in range(i):
        temp = gsum(i, j)
        res += temp
        ar[i].append(temp)
    if not res % 1000000:
        print(i)
        break
    if not i % 1000:
        print(i)
        
