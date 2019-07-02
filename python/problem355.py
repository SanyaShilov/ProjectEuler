import primes
LIMIT = 100
prime_list = primes.prime_list(LIMIT)
s = 1
st = {1}
for k in prime_list:
    p = k
    while p < LIMIT:
        p *= k
    p //= k
    st.add(p)
    s += p
print(s, st)


if __name__ == '__main__':
    print(main())
