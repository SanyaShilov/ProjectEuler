# C

import euler

LIMIT = 1000000

prime_list = euler.prime_list(LIMIT+1000)
s = 0
ten = 1
        
for i in range(2, len(prime_list)):
    pr1 = prime_list[i]
    if pr1 > LIMIT:
        break
    pr2 = prime_list[i+1]
    rest = pr2 - pr1
    if ten < pr1:
        ten *= 10
    start = ten
    while start % pr2 != rest:
        start += ten
    s += start + pr1
print(s)


if __name__ == '__main__':
    print(main())
