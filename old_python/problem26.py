import euler

prime_list = euler.prime_list(1000)
prime_list.remove(2)
prime_list.remove(5)

m = 0
val = 0
ten = 10
for pr in prime_list:
    while ten < pr:
        ten *= 10
    temp = ten
    while True:
        if (temp-1) % pr == 0:
            l = len(str((temp-1) // pr))
            if l > m:
                m = l
                val = pr
            break
        temp *= 10

print(val)
