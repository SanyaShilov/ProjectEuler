import array

def calc (b) :
    l = len(b)
    rf = b.rfind('1')
    if b.count('1') == 1 :
        return l-rf
    return calc(b[:rf])+(l-rf-1)*calc(b[:rf]+'0')

l = 10000

calced = array.array('L', (0 for i in range(l)))
calced[0] = 1

def numcalc (nn) :
    if nn < 1000000 :
        if calced[nn] :
            return calced[nn]
        if nn & 1 :
            return numcalc(nn >> 1)
        r = 0
        n = nn
        while not n & 1 :
            n >>= 1
            r += 1
        n >>= 1
        res = numcalc(n)+r*numcalc(n << 1)
        calced[nn] = res
        return res
    
    if nn & 1 :
        return numcalc(nn >> 1)
    if not nn :
        return 1
    r = 0
    while not nn & 1 :
        nn >>= 1
        r += 1
    nn >>= 1
    return numcalc(nn)+r*numcalc(nn << 1)

ar = [[i for i in range(2**j, 2**(j+1))] for j in range(7)]
car = [[numcalc(i) for i in k] for k in ar]
for k in car :
    print(k)


def wtf (j) :
	i = 0
	while j > 2**i-1 :
		i += 1
	return i

def first (j) :
	return 2**wtf(j)+j

def second (j) :
	return 2*2**wtf(j)+j

def pos (j, i) :
    return 2**(wtf(j)+i)+j

def diff (j) :
	return numcalc(second(j))-numcalc(first(j))

def KM (a, d) : # 123456789
    if d % 3 == 0 :
        if a % 3 :
            return (0, 0)
        if d % 9 == 0 :
            if a % 9 :
                return (0, 0)
    if d % 3607 == 0 :
        if a % 3607 :
            return (0, 0)
    if d % 3803 == 0 :
        if a % 3803 :
            return (0, 0)
    
'''
last = 0
b = 1
temp = 0
ten = 10
m = 0
for i in range(2000000):
    
    b += 1
    last = temp
    temp = numcalc(b)
    if temp > m :
        m = temp
    if temp % 987654321 == 0 :
        if abs(last/temp - 123456789/987654321) < 1e-3 :
            print(b)
            break
    if b > ten :
        print(ten)
        ten *= 10
print(m)
'''
