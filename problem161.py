# 000000000 * 12

import itertools

height = 12

little  = [int('000000001000000011', 2),
           int('000000011000000001', 2),
           int('000000011000000010', 2),
           int('000000010000000011', 2),
           int('000000000000000111', 2),
           int('000000001000000001000000001', 2)]


figures = []


for h in range(height-1) :
    for i in range(8) :
        figures.append(little[0] << i+9*h)

    for i in range(8) :
        figures.append(little[1] << i+9*h)

    for i in range(8) :
        figures.append(little[2] << i+9*h)

    for i in range(8) :
        figures.append(little[3] << i+9*h)

for h in range(height) :
    for i in range(7) :
        figures.append(little[4] << i+9*h)

for h in range(height-2) :
    for i in range(9) :
        figures.append(little[5] << i+9*h)

l = len(figures)


s = 0
ar = [0]
ind = [-1]
while ar :
    n = ar.pop()
    i = ind.pop()
    if n == 324518553658426726783156020576255 :
        s += 1
        continue
    for j in range(i+1, l) :
        if not n & figures[j] :
            ar.append(n | figures[j])
            ind.append(j)
print(s)
