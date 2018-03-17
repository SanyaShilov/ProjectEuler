import primes

limit = 10**8

eul = primes.euler_function_list(limit+1)

r = (limit*(limit+1)//2-sum(eul[:limit+1]))*6
print(r)
