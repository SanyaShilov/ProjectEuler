d = dict()
cubes = [c*c*c for c in range(1000)]
for i in range(1, 80000):
    i2 = i*i
    for j in range(1, 1000):
        a = i2+cubes[j]
        s = str(a)
        if s == s[::-1]:
            d[a] = d.get(a, 0) + 1
s = 0
n = 0
for k in d:
    if d[k] == 4:
        s += k
        n += 1
        if n == 5:
            break
print(s)
'''
('108909801', 4)
('5229225', 4)
('56200265', 4)
('37088073', 4)
('796767697', 4)
'''


if __name__ == '__main__':
    print(main())
