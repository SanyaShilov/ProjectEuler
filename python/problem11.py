ANSWER =


ar = [
    [int(c) for c in line.split()]
    for line in open('../txt/problem011.txt').readlines()
]
length = len(ar)
mx = 0
for i in range(length - 3):
    for j in range(length - 3):
        for prod in [
            ar[i][j] * ar[i][j + 1] * ar[i][j + 2] * ar[i][j + 3],
            ar[i][j] * ar[i + 1][j] * ar[i + 2][j] * ar[i + 3][j],
            ar[i][j] * ar[i + 1][1] * ar[i + 2][2] * ar[i + 3][3],
            ar[i + 3][j] * ar[i + 2][j + 1] * ar[i + 1][j + 2] * ar[i][j + 3]
        ]:
            mx = max(prod, mx)
print(mx)


if __name__ == '__main__':
    print(main())
