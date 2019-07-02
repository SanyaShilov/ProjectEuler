import primes

LIMIT = 40*10**6
eul = primes.euler_function_list(LIMIT)
print('done')
chains = [0, 1]

s = 0
for i in range(2, LIMIT):
    chains.append(chains[eul[i]]+1)
    if chains[-1] == 25:
        if eul[i] == i-1:
            s += i
print(s)


if __name__ == '__main__':
    print(main())
