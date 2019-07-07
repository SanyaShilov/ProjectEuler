ANSWER =


per = [set() for i in range(1500001)]
                
def wtf (p):
    q = p + 1
    p2 = p*p
    q2 = q*q
    while True:
        a = q2-p2
        b = 2*p*q
        c = q2+p2
        perimeter  = a + b + c
        if perimeter <= 1500000:
            a, b = min(a, b), max(a, b)
            for i in range(1, 1500000//perimeter+1):
                per[i*perimeter].add((a*i, b*i, c*i))
        else:
            break
        q += 1
        q2 = q*q

for i in range(1, 613):
    wtf(i)

result = 0
for i in range(len(per)):
    if len(per[i]) == 1:
        result += 1
print(result)


if __name__ == '__main__':
    print(main())
