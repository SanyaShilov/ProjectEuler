import sys


ANSWER =


def d_sum (n):
    s = str(n)
    l = len(s)
    r = 0
    for i in range(l):
        r += ord(s[i])
    return r - l*ord('0')

a1, a2 = 3, 1
b1, b2 = 8, 3
i = 3
step = 4
while True:
    for q in range(2):
        a1, b1 = b1, a1+b1
        a2, b2 = b2, a2+b2
        i += 1
        if i == 100:
            print(d_sum(b1))
            sys.exit()
    a1, b1 = b1, b1*step+a1
    a2, b2 = b2, b2*step+a2
    step += 2
    i += 1
    if i == 100:
        print(d_sum(b1))
        break


if __name__ == '__main__':
    print(main())
