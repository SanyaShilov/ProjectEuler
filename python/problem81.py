ANSWER =


ar = [[int(i) for i in k[:-1].split(',')] for k in open('../txt/problem081.txt').readlines()]
l = len(ar)
way = [[0 for i in range(l)] for j in range(l)]
way[0][0] = ar[0][0]
for i in range(1, l):
    way[0][i] = way[0][i-1] + ar[0][i]
    way[i][0] = way[i-1][0] + ar[i][0]
for i in range(1, l):
    for j in range(1, l):
        way[i][j] = min(way[i-1][j], way[i][j-1]) + ar[i][j]
print(way[l-1][l-1])


if __name__ == '__main__':
    print(main())
