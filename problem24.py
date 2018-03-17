def comb2 (m, n) : # размещения без повторений (выбрать m из n предметов с учетом порядка)
    return [] if m < 0 else [[]] if m == 0 else [c+[i] for c in comb2(m-1, n) for i in range(n) if i not in c]

c = comb2(10, 10)
s = 0
for k in c[999999] :
    s = s*10 + k
print(s)
