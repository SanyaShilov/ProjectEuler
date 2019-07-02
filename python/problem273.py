import primes

prime_list = primes.prime_list(150)

s = 0
p = 1
for pr in prime_list:
    if pr % 4 == 1:
        print(pr)
        p *= pr
        s += 1
print(s)
print(p)


if __name__ == '__main__':
    print(main())
