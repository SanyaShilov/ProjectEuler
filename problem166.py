def check (ar) :
    s = sum(ar[0])
    for i in range(1, 4) :
        if sum(ar[i]) != s :
            return False
    for i in range(4) :
        ss = 0
        for j in range(4) :
            ss += ar[j][i]
        if ss != s :
            return False
    ss = 0
    for i in range(4) :
        ss += ar[i][i]
    if ss != s :
        return False
    ss = 0
    for i in range(4) :
        ss += ar[3-i][i]
    if ss != s :
        return False
    return True
'''
ar = [[6, 3, 3, 0],
      [5, 0, 4, 3],
      [0, 7, 1, 4],
      [1, 2, 4, 5]]

ar1 = [[1, 1, 0, 0],
       [0, 0, 1, 1],
       [1, 1, 0, 0],
       [0, 0, 1, 1]]

ar2 = [[0, 0, 1, 1],
       [1, 1, 0, 0],
       [0, 0, 1, 1],
       [1, 1, 0, 0]]

ar3 = [[1, 0, 0, 1],
       [0, 1, 1, 0],
       [1, 0, 0, 1],
       [0, 1, 1, 0]]

ar4 = [[1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0],
       [0, 1, 1, 0]]

'''

s = 0
for n in range(2**16) :
    ar = [[0 for i in range(4)] for j in range(4)]
    for i in range(4) :
        for j in range(4) :
            ar[i][j] = n&1
            n >>= 1
    if check(ar) :
        s += 1
        if ar[0] == [1, 0, 0, 0] :
            for k in ar :
                print(k)
            print()
print(s)
