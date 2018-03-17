import array

def isprime (n, primelist) :
    sq = int(n**0.5)
    i = 0
    for pr in primelist :
        if pr > sq :
            return True
        if not n % pr :
            return False

def primelist (n) :
    index = array.array('L', (1 for i in range(n)))
    result = array.array('L')
    i = 2
    while i < n :
        if index[i] :
            result.append(i)
            j = i
            while j < n :
                index[j] = 0
                j += i
        i += 1
    return result



def totientlist (n) :
    result = [i for i in range(n)]
    for i in range(2, n) :
        if result[i] == i :
            for j in range(i, n, i) :
                result[j] -= result[j] // i
    return result

def gcd1 (a, b) :
    ''' a > 1 '''
    if a == 1 :
        return True
    if not a :
        return False
    if a > b :
        return gcd1(a%b, b)
    return gcd1(b%a, a)

def pythagor (a) :
    a2 = a*a
    for b in range(1, a) :
        b2 = b*b
        yield a2-b2, 2*a*b, a2+b2

def pythagorUnique (a) :
    a2 = a*a
    for b in range(1, a) :
        b2 = b*b
        x = a2-b2
        y = 2*a*b
        if gcd1(x, y) :
            yield x, y, a2+b2

def parsefraction (lst) :
	b = 1
	a = lst[-1]
	for i in range(len(lst)-1) :
		c = a
		a = a*lst[-2-i]+b
		b = c
	return a, b

def squarefraction (nn, leng) :
    sq = nn**0.5
    tr = int(sq)
    start = add = -tr
    d = 1
    l = 0
    lst = []
    while True :
        lst.append(tr)
        l += 1
        wtf = nn-add*add
        d = wtf//d
        tr = int((sq-add)/d)
        add = -add - tr*d
        if l > leng :
            break
    return lst

def notdivisible (num, ar, ind) :
    ''' ind = len(ar)'''
    res = num
    for i in range(ind) :
        r = num//ar[i]
        if not r :
            break
        res -= notdivisible(r, ar, i)
    return res

def pandigital (n) :
    ar = [False for i in range(10)]
    while n :
        r = n % 10
        if ar[r] :
            return False
        ar[r] = True
        n //= 10
    return True

if __name__ == '__main__':
    pass