def fill (n): #  нечетное
    tab = [[0 for i in range(n)] for j in range(n)]
    c = n // 2
    tab[c][c] = 1
    num = 2
    for i in range (2, n, 2):
        for j in range(i):
            tab[c+1-i//2+j][c+i//2] = num
            num += 1
        for j in range(i):
            tab[c+i//2][c+i//2-1-j] = num
            num += 1
        for j in range(i):
            tab[c-j+i//2-1][c-i//2] = num
            num += 1
        for j in range(i):
            tab[c-i//2][c+j-i//2+1] = num
            num += 1
    return tab

t = fill(1001)
s = 0
for i in range(1001):
    s += t[i][i]
    s += t[1000-i][i]
print(s-1)
