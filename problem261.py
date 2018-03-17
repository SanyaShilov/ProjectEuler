a, b = 2, 1
while True :
    a2 = a*a
    b2 = b*b
    a2b2m = a2-b2
    ab = 2*a*b
    a2b2p = a2+b2
    a2b2m, ab = min(a2b2m, ab), max(a2b2m, ab)
    if ab > 10**10 :
        break
    print(a2b2m, ab, a2+b2)
    a, b = 2*a+b, a

sq = [i*i for i in range(20000)]
sq2 = [sq[i]+sq[i+1] for i in range(19999)]
sq3 = [sq[i]+sq[i+1]+sq[i+2] for i in range(19998)]
sq4 = [sq[i]+sq[i+1]+sq[i+2]+sq[i+3] for i in range(19997)]
sq5 = [sq[i]+sq[i+1]+sq[i+2]+sq[i+3]+sq[i+4] for i in range(19996)]
for i in range(19996) :
    if sq5[i] in sq4 :
        print(i, sq4.index(sq5[i]))
