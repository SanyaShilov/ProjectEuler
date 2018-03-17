import primes

limit = 40*10**6
eul = primes.euler_function_list(limit)
print('done')
chains = [0, 1]

s = 0
for i in range(2, limit) :
    chains.append(chains[eul[i]]+1)
    if chains[-1] == 25 :
        if eul[i] == i-1 :
            s += i
print(s)
