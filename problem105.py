ar = [sorted([int(k) for k in l.split(',')]) for l in open('p105.txt').readlines()]
s = 0

def test1 (st) :
    for i in range(len(st)//2) :
        if sum(st[:i+2]) == sum(st[-1-i:]) :
            return False
    return True

def test2 (st) :
    for i in range(len(st)//2) :
        if sum(st[:i+2]) <= sum(st[-1-i:]) :
            return False
    return True
n = 0
for st in ar :
    save = st[:]
    sa = sum(st)
    l = len(st)
    l2 = l//2
    if test2(st) :
        while st :
            if test1(st) :
                st = [k-min(st) for k in st[1:]]
            else :
                break
        if not st :
            print(save, ar.index(save))
            s += sa
            n += 1
print(s, n)
