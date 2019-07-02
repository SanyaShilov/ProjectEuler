ANSWER =


def parse (lst):
	b = 1
	a = lst[-1]
	for i in range(len(lst)-1):
		c = a
		a = a*lst[-2-i]+b
		b = c
	return a, b

def calc (nn, leng):
    sq = nn**0.5
    tr = int(sq)
    start = add = -tr
    d = 1
    l = 0
    lst = []
    while True:
        lst.append(tr)
        l += 1
        wtf = nn-add*add
        d = wtf//d
        tr = int((sq-add)/d)
        add = -add - tr*d
        if l > leng:
            break
    return lst 

sq = [i*i for i in range(40)]
D = [i for i in range(1000+1) if i not in sq]
l = len(D)
X = [0 for i in range(l)]
Y = [0 for i in range(l)]
for i in range(l):
    d = D[i]
    dsq = d**0.5
    lst = calc(d, 1000)
    for j in range(1, 1000):
        x, y = parse(lst[:j])
        if x/y < dsq:
            x += 1
        if x*x-d*y*y == 1:
            X[i] = x
            Y[i] = y
            break
print(D[X.index(max(X))])


if __name__ == '__main__':
    print(main())
