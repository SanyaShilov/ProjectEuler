ANSWER =


def find (n):
    rest = 1
    i = 1
    while rest:
        rest = (rest*10 + 1) % n
        i += 1
    return i

n = 10**6
while True:
    n += 1
    if n % 2 and n % 5:
        if find(n) > 10**6:
            print(n)
            break


if __name__ == '__main__':
    print(main())
