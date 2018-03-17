# dynamic programming

limit = 100

ar = [[0 for i in range(limit+1)] for j in range(limit+1)]
ar[0][0] = 1
for i in range(1, limit+1) :
    for j in range(i) :
        ar[i][j] = sum(ar[i-j-1][:j+1])
print(sum(ar[limit])-1)
