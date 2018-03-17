def ispalindrom (n) :
    s = str(n)
    return s == s[::-1]

m = 0
for i in range(100, 1000) :
    for j in range(i, 1000) :
        p = i*j
        if p > m :
            if ispalindrom(p) :
                m = p
print(m)
