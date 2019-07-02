ANSWER =


m = 1
while True:
    s = set(str(m))
    for i in range(2, 7):
        if s != set(str(m*i)):
            break
    else:
        print(m)
        break
    m += 1


if __name__ == '__main__':
    print(main())
