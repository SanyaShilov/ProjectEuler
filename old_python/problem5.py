import euler

LIMIT = 20
prime_list = euler.prime_list(LIMIT+1)
result = 1
for i in range(len(prime_list)):
    pr = prime_list[i]
    while pr < LIMIT:
        pr *= prime_list[i]
    pr //= prime_list[i]
    result *= pr
print(result)
    
