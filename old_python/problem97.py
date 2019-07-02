a = 1
mod = 10**10
for i in range(7830457):
    a = (a << 1) % mod
a = a * 28433 + 1
print(a % mod)
