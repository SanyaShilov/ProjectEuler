import euler
import array

prime_list = euler.prime_list(1000000)

lst = array.array('L', (0 for i in range(10000000)))

for pr in prime_list:
    lst[pr] = 1

s = 0
for i in range(1, 600):
    pr = 3*i*i-3*i+1
    if lst[pr]:
        s += 1
print(s)
