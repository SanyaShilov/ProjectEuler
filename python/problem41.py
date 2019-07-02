import euler


ANSWER =


prime_list = euler.prime_list(10**7) # 1 to 8 and 1 to 9 pandigital can't be prime
                                   # because its divisible by 9

def pandig (n):
    s = set()
    l = len(str(n))
    while n:
        r = n % 10
        if not r:
            return False
        if r > l:
            return False
        if r in s:
            return False
        s.add(r)
        n //= 10
    return True

for pr in prime_list[::-1]:
    if pandig(pr):
        print(pr)
        break


if __name__ == '__main__':
    print(main())
