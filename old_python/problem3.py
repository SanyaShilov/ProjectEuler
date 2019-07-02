n = 600851475143
pr = 2
while pr < n:
    if not n % pr:
        n //= pr
        pr -= 1
    pr += 1
print(n)
