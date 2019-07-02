s = set()
for i in range(10, 100):
    for j in range(100, 1000):
        k = i*j
        sk = str(k)
        if len(sk) == 4:
            st = set(str(i)+str(j)+sk)
            if '0' not in st:
                if len(st) == 9:
                    s.add(k)
for i in range(1, 10):
    for j in range(1000, 10000):
        k = i*j
        sk = str(k)
        if len(sk) == 4:
            st = set(str(i)+str(j)+sk)
            if '0' not in st:
                if len(st) == 9:
                    s.add(k)
print(sum(s))
