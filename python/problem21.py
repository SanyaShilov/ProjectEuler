import euler


ANSWER =


s = 0
for i in range(2, 10000):
    d = euler.sum_divisors(i)
    if d != i:
        if euler.sum_divisors(d) == i:
            s += i
print(s)


if __name__ == '__main__':
    print(main())
