ANSWER =


def step (n):
    return n + int(str(n)[::-1])

def is_p (n):
    s = str(n)
    return s == s[::-1]

s = 0
for i in range(1, 10000):
    c = step(i)
    temp = 1
    d = 0
    while temp < 51:
        if is_p(c):
            d = 1
            break
        c = step(c)
        temp += 1
    if d == 0:
        s += 1
print(s)


if __name__ == '__main__':
    print(main())
