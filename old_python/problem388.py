LIMIT = 10**2 + 1

lst = [1]
for i in range(2, LIMIT + 1):
    lst.append(i**3 - (i-1)**3)
print(lst[:20])
ar2 = lst.copy()
for i in range(1, LIMIT // 2 + 1):
    a = ar2[i]
    for j in range(i + i, LIMIT, i):
        ar2[j] -= a
print(ar2[:20])
print(sum(ar2) - 1)
print([lst[i] - ar2[i] for i in range(20)])
