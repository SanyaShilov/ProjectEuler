import euler

s = 0
for n in range(4, 1000000000 // 3 + 3, 2) :
    p1, p2 = 3*n + 2, 3*n - 2
    c1, c2 = p1*(n+2), p2*(n-2)
    if c1 == round(c1**0.5)**2 :
        s += p1
    if c2 == round(c2**0.5)**2 :
        s += p2
print(s)
# 11138120726
# 518408346 !!!
