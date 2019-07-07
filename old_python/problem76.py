LIMIT = 100

lst = [[0 for i in range(LIMIT+1)] for j in range(LIMIT+1)]
lst[0][0] = 1
for i in range(1, LIMIT+1):
    for j in range(i):
        lst[i][j] = sum(lst[i-j-1][:j+1])
print(sum(lst[LIMIT])-1)
