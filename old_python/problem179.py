import primes
'''
prime_list = primes.prime_list(10000)

squares = [i*i for i in range(1, 10000)]
'''


lst = [0 for i in range(10000000+1)]
for i in range(2, 3163):
    if i % 100 == 0:
        print(i)
    for j in range(i*i, 10000000+1, i):
        lst[j] += 2
    lst[i*i] -= 1

res = 0
for i in range(2, 10000000):
    if lst[i] == lst[i+1]:
        res += 1
print(res)
