ar = open('p059.txt').readlines()
ar = ar[0].split(',')
ar = [int(k) for k in ar]
m = [0, 1, 2]
meet = set()
for k in ar :
    if k in meet :
        continue
    meet.add(k)
    c = ar.count(k)
    if c > min(m) :
        m = [q for q in m if q != min(m)]+[c]
meet = set()
for k in ar :
    if k in meet :
        continue
    meet.add(k)
    if ar.count(k) in m :
        pass
sm = 0
for i in range(len(ar)) :
	if i%3 == 0 :
		sm += ar[i]^103
	if i%3 == 1 :
		sm += ar[i]^111
	if i%3 == 2 :
		sm += ar[i]^100
print(sm)
