ANSWER =


a = -1
ten = 10**-9
for i in range(600):
    b = int(2**(30.403243784 - a*a))*ten
    print(a+b)
    a = b


if __name__ == '__main__':
    print(main())
