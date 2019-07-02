ANSWER =


a1, a2 = 3, 2
b1, b2 = 7, 5
i = 2
s = 0
while i <= 1000:
    a1, b1 = b1, b1*2+a1
    a2, b2 = b2, b2*2+a2
    i += 1
    if len(str(b1)) > len(str(b2)):
        s += 1
print(s)


if __name__ == '__main__':
    print(main())
