import euler

prime_list = euler.prime_list(1000000)

q22 = 4
q25 = 25
q23 = 8
q53 = 125

s = []
for pr in prime_list:
    pr2 = pr*pr
    pr3 = pr2*pr
    st = str(pr2*q23)
    if '200' in st:
        s.append(int(st))
    st = str(pr2*q53)
    if '200' in st:
        s.append(int(st))
    st = str(pr3*q22)
    if '200' in st:
        s.append(int(st))
    st = str(pr3*q25)
    if '200' in st:
        s.append(int(st))
s.sort()
print(s[5], s[50], s[100], s[200])
