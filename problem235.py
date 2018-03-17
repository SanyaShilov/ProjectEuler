def u (r, k) :
    return (900-3*k)*r**(k-1)

def s (n, r) :
    s = 0
    for k in range(1, n+1) :
        s += u(r, k)
    return s

r = 1
ten = 0.1
need = -600000000000
ss = s(5000, r)
for i in range(20):
    if ten < 1e-15 :
        break
    ss = s(5000, r)
    while ss > need :
        r += ten
        ss = s(5000, r)
    r -= ten
    ten /= 10
    print(r, s(5000, r))
print(round(r, 12))
