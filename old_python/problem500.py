import euler
prime_list = euler.prime_list(7376513) # 500500 primes
l = len(prime_list)
lst = [1 for i in range(l)]
pb = 0
pe = l-1
while lst[pb]:
    pw1 = lst[pb]+1
    if prime_list[pb]**pw1 < prime_list[pe]:
        lst[pe] = 0
        lst[pb] += pw1
        pe -= 1
    else:
        pb += 1
n = 1
for i in range(l):
    n = (n*prime_list[i]**lst[i])%500500507
print(n)
