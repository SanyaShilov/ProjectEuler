import array


ANSWER =


l = 101

#more than 30000



lst = [[0 for i in range(l)] for j in range(l)]
lst[0][0] = 1
for i in range(1, l):
    for j in range(i):
        lst[i][j] = sum(lst[i-j-1][:j+1])

l = 101

r = range(l+1)

summed = [array.array('L', (1,)) for i in r]

def gsum (i, j):
    global lst, summed
    ind = i-j-1
    if j >= ind:
        return summed[ind][-1]
    if j == 0:
        return 1
    temp = (summed[ind][j-1]+lst[ind][j])%1000000
    summed[ind].append(temp)
    return temp


lst = [array.array('L') for i in r]
print('done')
lst[0].append(1)
i = 1
for i in range(1, l+1):
    result = 0
    for j in range(i):
        temp = gsum(i, j)
        result += temp
        lst[i].append(temp)
    if not result % 1000000:
        print(i)
        break
    if not i % 1000:
        print(i)


if __name__ == '__main__':
    print(main())
