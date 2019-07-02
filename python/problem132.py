# about 10 munites

import euler

def find (n):
    rest = 1
    i = 1
    while rest:
        rest = (rest*10 + 1) % n
        i += 1
    return i

prime_list = euler.prime_list(1000000)
prime_list.remove(2)
prime_list.remove(5)

s = 0
big = 10**9
count = 0
for pr in prime_list:
    if big % find(pr) == 0:
        count += 1
        s += pr
        if count == 40:
            break
print(s)


if __name__ == '__main__':
    print(main())
