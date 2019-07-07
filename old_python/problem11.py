lst = open('../txt/problem011.txt').readlines()
lst = [k.split() for k in lst]
lst = [[int(c) for c in k] for k in lst]
l = len(lst)
m = 0
for i in range(l-3):
    for j in range(l-3):
        pr = lst[i][j] * lst[i][j+1] * lst[i][j+2] * lst[i][j+3]
        if pr > m:
            m = pr
        pr = lst[i][j] * lst[i+1][j] * lst[i+2][j] * lst[i+3][j]
        if pr > m:
            m = pr
        pr = lst[i][j] * lst[i+1][1] * lst[i+2][2] * lst[i+3][3]
        if pr > m:
            m = pr
        pr = lst[i+3][j] * lst[i+2][j+1] * lst[i+1][j+2] * lst[i][j+3]
        if pr > m:
            m = pr
print(m)
