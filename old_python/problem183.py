def terminating (n):
    while not n&1:
        n >>= 1
    while not n%5:
        n //= 5
    if n != 1:
        return False
    return True


s = 0
rk = 1
for n in range(5, 10001):
    m = 0
    if (n/rk) < (n/(rk+1))**((rk+1)/rk):
        rk += 1
    nn = rk
    while not nn&1:
        nn >>= 1
    while not nn%5:
        nn //= 5
    if n % nn:
        s += n
    else:
        s -= n
print(s)
