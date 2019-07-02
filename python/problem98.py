ANSWER =


f = open('../txt/problem098.txt')
r = f.readlines()
s = r[0]
ar = s.split('","')
ar[0] = ar[0].replace('"', '')
ar[-1] = ar[-1].replace('"', '')

d = dict()

for i in range(1, 15):
    d[i] = []

for k in ar:
    d[len(k)].append(k)

words = []

def WordAnagram (a, b):
    for k in a:
        if a.count(k) != b.count(k):
            return False
    return True

def WordMask (w):
    s = set(w)
    mask = {l: [] for l in s}
    for k in range(len(w)):
        mask[w[k]].append(k)
    return mask

def SuitMask (sm, wm):
    for l in wm.values():
        if l not in sm.values():
            return False
    return True

def Form (s, w, w2):
    d = {l: 0 for l in w}
    for l in w[::-1]:
        d[l] = s % 10
        s //= 10
    res = 0
    for l in w2:
        res = res*10+d[l]
    return res

for i in range(1, 15):
    l = len(d[i])
    for j in range(l):
        for k in range(j+1, l):
            if WordAnagram(d[i][j], d[i][k]):
                words.append([d[i][j], d[i][k]])

sq = []
j = 1
for i in range(10):
	sq.append([])
	ten = 10**i
	while j*j < ten:
		sq[i].append(j*j)
		j += 1

suit = []
i = 0
res = 0
for dw in words:
    w = dw[0]
    w2 = dw[1]
    l = len(w)
    suit.append([])
    wm = WordMask(w)
    wm2 = WordMask(dw[1])
    for s in sq[l]:
        sm = WordMask(str(s))
        if SuitMask(sm, wm):
            suit[i].append(s)
            s2 = Form(s, w, w2)
            if s2 in sq[l]:
                if s2 > res:
                    res = s2
    i += 1
print(res)

    
if __name__ == '__main__':
    print(main())
