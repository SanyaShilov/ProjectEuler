import euler

def find (n):
    rest = 1
    i = 1
    while rest:
        rest = (rest*10 + 1) % n
        i += 1
    return i

l= 30000

prime_list = euler.prime_list(l)

lst = [i for i in range(l)]
lst[1] = 0

for pr in prime_list:
    lst[pr] = 0

for i in range(2, l, 2):
    lst[i] = 0

for i in range(5, l, 5):
    lst[i] = 0

s = 0
i = 0
for k in lst:
    if k:
        f = find(k)
        if (k-1) % f == 0:
            i += 1
            s += k
            if i == 25:
                break
print(s)
