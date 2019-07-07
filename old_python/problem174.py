
lst = [i**2 for i in range(250002)]
used = [0 for i in range(1000001)]
for i in range(3, 250002):
    if i % 1000 == 0:
        print(i)
    if i < 1001:
        min_cub = 0
        min_j = 0
    else:
        min_cub = lst[i] - 1000000
        m = int(min_cub**0.5)
        min_j = m - m%2 - i%2
    r = range(max(2 - i%2, min_j), i, 2)
    passed = 0
    for j in r:
        if lst[j] < min_cub:
            passed += 1
            continue
        used[lst[i]-lst[j]] += 1
s = 0
for i in range(1000001):
    if used[i] > 0 and used[i] < 11:
        s += 1
print(s)
