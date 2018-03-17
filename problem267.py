n = 1000
limit = 10**9
power = 1000

mp = 1000
mq = 0
for i in range(0, 20) :
    power = 500
    q = 0.145 + i * 0.0001
    q2 = q+q
    while True :
        if (1+q2)**power * (1-q)**(n-power) < limit :
            print(q, power, (1+q2)**power * (1-q)**(n-power))
            print((1+q2)**(power+1) * (1-q)**(n-power-1))
            if power < mp :
                mp = power
                mq = q
            break
        power -= 1
print(mp, mq)
