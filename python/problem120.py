ANSWER =


mm = 0
for a in range(3, 1001):
    aa = a**2
    m = 0
    for n in range(3, 2001, 2):
        num = 2*a*n
        r = num % aa
        if r > m:
            m = r
    mm += m
print(mm)


if __name__ == '__main__':
    print(main())
