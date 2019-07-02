ANSWER =


n = 2**1000
s = 0
while n:
    s += n % 10
    n //= 10
print(s)


if __name__ == '__main__':
    print(main())
