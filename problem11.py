ar = open('p011.txt').readlines()
ar = [k.split() for k in ar]
ar = [[int(c) for c in k] for k in ar]
l = len(ar)
m = 0
for i in range(l-3) :
    for j in range(l-3) :
        pr = ar[i][j] * ar[i][j+1] * ar[i][j+2] * ar[i][j+3]
        if pr > m :
            m = pr
        pr = ar[i][j] * ar[i+1][j] * ar[i+2][j] * ar[i+3][j]
        if pr > m :
            m = pr
        pr = ar[i][j] * ar[i+1][1] * ar[i+2][2] * ar[i+3][3]
        if pr > m :
            m = pr
        pr = ar[i+3][j] * ar[i+2][j+1] * ar[i+1][j+2] * ar[i][j+3]
        if pr > m :
            m = pr
print(m)
