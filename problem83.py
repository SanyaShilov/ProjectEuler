# dynamic programming

ar = open('p083.txt').readlines()
ar = [k.split(',') for k in ar]
tab = [[int(c) for c in k] for k in ar]

l = len(tab)
way = [[100000000 for i in range(l)] for j in range(l)]
way[0][0] = tab[0][0]

def it (tab, way) :
    l = len(tab)
    for i in range(1, l) :
        way[0][i] = min(way[0][i-1], way[1][i]) + tab[0][i]
        way[i][0] = min(way[i-1][0], way[i][1]) + tab[i][0]
    for i in range(1, l-1) :
        for j in range(1, l-1) :
            way[i][j] = min(way[i-1][j], way[i][j-1], way[i+1][j],
                            way[i][j+1]) + tab[i][j]
    for i in range(1, l) :
        way[i][l-1] = min(way[i-1][l-1], way[i][l-2]) + tab[i][l-1]
        way[l-1][i] = min(way[l-1][i-1], way[l-2][i]) + tab[l-1][i]

for i in range(1000) :
    it(tab, way)
print(way[l-1][l-1])
