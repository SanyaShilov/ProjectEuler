import array
import sys
import timeit

def pandig (n) :
    s = [0 for i in range(10)]
    while n :
        nn = n % 10
        if not nn :
            return False
        if s[nn] :
            return False
        s[nn] = 1
        n //= 10
    return True

def pandigstr (st) :
    s = set()
    for k in st :
        if k in s :
            return False
        s.add(k)
    return True

def prime_list (n) :
    index = array.array('L', (1 for i in range(n)))
    result = array.array('L')
    i = 2
    while i < n :
        if index[i] :
            j = i+i
            while j < n :
                index[j] = 0
                j += i
            if pandig(i) :
                result.append(i)
        i += 1
    return result

lst = prime_list(10**8)
strlst = [str(p) for p in lst]
s = 0
arstr = ['']
arind = [-1]
l = len(strlst)
while arstr :
    st = arstr.pop()
    ind = arind.pop()
    for i in range(ind+1, l) :
        new = st+strlst[i]
        ln = len(new)
        if ln > 9 :
            break
        if pandigstr(new) :
            if ln == 9 :
                s += 1
            else :
                arstr.append(new)
                arind.append(i)
print(s)



