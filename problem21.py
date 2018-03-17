def all_div (n) :
    d = 0
    for i in range(1, n//2+1) :
        if n % i == 0 :
            d += i
    return d
s = 0
for i in range(2, 10000) :
    d = all_div(i)
    if d != i :
        if all_div(d) == i :
            s += i
print(s)
