ANSWER =


ar = open('../txt/problem082.txt').readlines()
ar = [k.split(',') for k in ar]
tab = [[int(c) for c in k] for k in ar]
l = len(tab)
way = [[0 for i in range(l)] for j in range(l)]

def it (tab, way, n):
    l = len(way)
    for j in range(l):
        way[0][n] = min(way[0][n-1], way[1][n]) + tab[0][n]
        for i in range(1, l-1):
            way[i][n] = min(way[i-1][n], way[i][n-1], way[i+1][n]) + tab[i][n]
        way[l-1][n] = min(way[l-2][n], way[l-1][n-1]) + tab[l-1][n]
        
for i in range(l):
    way[i][0] = tab[i][0]

for i in range(1, l):
    for j in range(l):
        way[j][i] = way[j][i-1] + tab[j][i]
    it(tab, way, i)


end = [k[-1] for k in way]
print(min(end))


if __name__ == '__main__':
    print(main())
