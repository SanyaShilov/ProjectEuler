ANSWER =


LIMIT = 100

ar = [[0 for i in range(LIMIT+1)] for j in range(LIMIT+1)]
ar[0][0] = 1
for i in range(1, LIMIT+1):
    for j in range(i):
        ar[i][j] = sum(ar[i-j-1][:j+1])
print(sum(ar[LIMIT])-1)


if __name__ == '__main__':
    print(main())
