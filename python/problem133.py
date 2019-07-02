import euler

def find (n):
    rest = 1
    i = 1
    while rest:
        rest = (rest*10 + 1) % n
        i += 1
    return i

prime_list = euler.prime_list(100000)
prime_list.remove(2)
prime_list.remove(5)

res = 0
for pr in prime_list:
    ff = f = find(pr)
    while f % 2 == 0:
        f >>= 1
    while f % 5 == 0:
        f //= 5
    if f == 1:
        res += pr
print(sum(prime_list)-res+2+5)


if __name__ == '__main__':
    print(main())
