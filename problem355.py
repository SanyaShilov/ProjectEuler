import primes
limit = 100
primelist = primes.prime_list(limit)
s = 1
st = {1}
for k in primelist :
    p = k
    while p < limit :
        p *= k
    p //= k
    st.add(p)
    s += p
print(s, st)
