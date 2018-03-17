import primes

primelist = primes.prime_list(5000)


ways = [0 for i in range(sum(primelist)+1)]
ways[0] = 1

biglist = primes.prime_list(sum(primelist)+1)

st = {0}
for pr in primelist :
    print(pr)
    newways = ways[:]
    for n in st.copy() :
        nn = pr + n
        newways[nn] += ways[n]
        st.add(nn)
    ways = newways
s = 0
for pr in biglist :
    s += ways[pr]
print(s)


#2493013197774260
