
mx = 10**100
st = []
for a in range(6) :
    for b in range(6) :
        for c in range(5) :
            for d in range(3) :
                for e in range(3) :
                    for f in range(3) :
                        for g in range(3) :
                            for h in range(2) :
                                for i in range(2) :
                                    for k in range(2) :
                                        for l in range(2) :
                                            for m in range(2) :
                                                dn = (a+a+1)*(b+b+1)*(c+c+1)*(d+d+1)*(e+e+1)*(f+f+1)*(g+g+1)*(h+h+1)*(i+i+1)*(k+k+1)*(l+l+1)*(m+m+1)
                                                if (dn+1)//2 > 1000 :
                                                    n = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f * 17**g * 19**h * 23**i * 29**k * 31**l * 37**m
                                                    if n < mx :
                                                        mx = n


print(mx)
