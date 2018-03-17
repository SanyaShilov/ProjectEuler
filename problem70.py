import euler

lst = euler.totientlist(10000000)

def is_permutation (a, b) :
    s = []
    while a :
        s.append(a % 10)
        a //= 10
    try :
        while b :
            s.remove(b % 10)
            b //= 10
        if s :
            return False
        return True
    except :
        return False
    
minimum = 10000
n = 0
for i in range(2, 10000000) :
    fi = lst[i]
    if is_permutation(fi, i) :
        m = i/fi
        if m < minimum :
            minimum = m
            n = i
print(n)
