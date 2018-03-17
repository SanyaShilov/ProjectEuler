import euler

primelist = euler.primelist(1000)
primelist.remove(2)
primelist.remove(5)

m = 0
val = 0
ten = 10
for pr in primelist :
    while ten < pr :
        ten *= 10
    temp = ten
    while True :
        if (temp-1) % pr == 0 :
            l = len(str((temp-1) // pr))
            if l > m :
                m = l
                val = pr
            break
        temp *= 10

print(val)
